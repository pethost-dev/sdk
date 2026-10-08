# Pethost for Python

The Python SDK for [Pethost](https://pethost.dev), hosting for Docker Compose projects on a
machine of your own. It has the 13 calls of Pethost's API, the ones an agent has through its
MCP server: read the machine and its projects, deploy, read logs and HTTP requests, run
commands, move files. It has the API's streams too, which follow an operation, the logs
and the requests as they happen. Everything is typed, there is a synchronous client and an
asyncio one, and the whole package is generated from the API's definition, so its methods, its
fields and their documentation are the API's own.

## Install

```sh
pip install pethost
```

Python 3.10 or newer. With uv: `uv add pethost`.

## A token

The SDK signs in with an API token. Make one in [the panel](https://console.pethost.dev)'s
Settings, under "API tokens", and give it to the SDK in the environment variable
`PETHOST_TOKEN`, or as the client's first argument. A token acts as you: keep it out of your
code and your repository.

## A first program

It reads the machine and its projects, then deploys to the project `notes` by writing one
file, `/hello.txt`.

```python
from pethost import FileChange, Pethost

with Pethost() as pethost:  # The token: PETHOST_TOKEN.
    answer = pethost.get_machine()
    machine = answer.machine
    if machine is None:
        raise SystemExit("the answer has no machine")

    print(machine.hostname)
    for project in answer.projects:
        print(project.project_id)

    deployed = pethost.deploy_project(
        "notes",
        files=[FileChange(path="/hello.txt", text="Hello from the Pethost SDK\n")],
    )
    for violation in deployed.violations:  # The file was refused: nothing was deployed.
        print(violation.location, violation.violation_message)

    if deployed.operation is not None:
        print(deployed.operation.status.name)
    if deployed.project is not None:  # The project as it is once the deploy ended.
        print(deployed.project.url)
```

`AsyncPethost` has the same methods for asyncio:

```python
import asyncio

from pethost import AsyncPethost


async def main() -> None:
    async with AsyncPethost() as pethost:
        print(await pethost.get_machine())


asyncio.run(main())
```

## Methods

| Method | What it does | |
|---|---|---|
| `get_machine()` | Get the machine | read-only |
| `run_machine_action(...)` | Run a machine action | destructive |
| `get_project(project_id, ...)` | Get a project | read-only |
| `create_project(project_id, ...)` | Create a project |  |
| `deploy_project(project_id, ...)` | Deploy a project | destructive |
| `list_commits(project_id, ...)` | List a project's commits | read-only |
| `run_project_action(project_id, ...)` | Run a project action | destructive |
| `get_operation(project_id, ...)` | Get an operation | read-only |
| `query_http_traffic(project_id, ...)` | Query HTTP traffic | read-only |
| `query_container_logs(project_id, ...)` | Query container logs | read-only |
| `run_service_command(project_id, ...)` | Run a command in a service | destructive |
| `read_path(project_id, ...)` | Read a file or directory | read-only |
| `create_transfer(...)` | Upload or download a file | destructive |
| `watch_operation(project_id, ...)` | Watch an operation | stream |
| `tail_container_logs(project_id, ...)` | Follow container logs | stream |
| `tail_http_traffic(project_id, ...)` | Follow HTTP traffic | stream |

A read-only call changes nothing; a destructive one may delete or overwrite something; a stream
returns its responses one by one, as "Streams" below shows. A request's fields are its method's
keyword arguments, a message is a frozen dataclass of the same name, and each docstring is the
API's own description: `help(Pethost)` and your editor show it. What the API calls absent is
`None` where a type allows `None`, and the zero value anywhere else.

## Streams

A stream is a method that returns a generator: read it with `for`, and each response comes as
the API sends it, for as long as the loop runs. This program prints a project's newest log
lines, then follows them.

```python
from pethost import Pethost

with Pethost() as pethost:
    # The newest lines, and where a stream goes on from them without missing one.
    newest = pethost.query_container_logs("notes")
    for line in newest.lines:
        print(line.service, line.text)

    # Each later line as it is written. The loop runs until the stream fails, which raises; to
    # stop it sooner, leave the loop.
    for response in pethost.tail_container_logs("notes", after_cursor=newest.tail_cursor):
        if response.line is not None:
            print(response.line.service, response.line.text)
```

The call is made when the loop starts. A stream that fails raises its `PethostError` from the
loop, once, after the responses that came before it; one that ends by itself just ends the
loop. Leaving the loop ends the call: Python closes a generator that nothing else holds. Where
a variable holds it, its `close()` ends the call, and so does `contextlib.closing` around it.
The client's `timeout` does not bound a stream, and the package does not call again by itself:
where a response carries a cursor, as a log line does, a new call goes on from it.

While this client waits for a response, Python does not act on Ctrl-C: `KeyboardInterrupt` is
raised when the API next sends something. That is the next response or, on a quiet stream, what
the API sends through a silence to keep the stream open, which the loop never sees. A program that
must stop at once reads the stream with `AsyncPethost`.

`AsyncPethost` has each stream as an asynchronous generator, read with `async for`:

```python
import asyncio

from pethost import AsyncPethost


async def main() -> None:
    async with AsyncPethost() as pethost:
        async for response in pethost.tail_container_logs("notes"):  # From now on.
            if response.line is not None:
                print(response.line.service, response.line.text)


asyncio.run(main())
```

Leaving that loop ends the call on the event loop's next turn. Cancelling the task ends it too,
so Ctrl-C stops the program at once, and `asyncio.wait_for` can bound the reading by time.
Where a variable holds the generator, `await` its `aclose()`, or put `contextlib.aclosing`
around it.

## Errors

A failed call raises a `PethostError`, and its class is the code:
`CanceledError`, `UnknownError`, `InvalidArgumentError`, `DeadlineExceededError`, `NotFoundError`, `AlreadyExistsError`, `PermissionDeniedError`, `ResourceExhaustedError`, `FailedPreconditionError`, `AbortedError`, `OutOfRangeError`, `UnimplementedError`, `InternalError`, `UnavailableError`, `DataLossError`, `UnauthenticatedError`.
`error.message` is prose for people. What a program branches on, beside the class, is
`error.detail`: `ProjectBusy`, `ProjectChanged`, `MachineUnreachable`, `NoMachine`, or `None`.

```python
from pethost import NotFoundError, Pethost, PethostError

with Pethost() as pethost:
    try:
        project = pethost.get_project("notes").project
    except NotFoundError as error:
        print(error.message)  # No such project: the message lists the ones there are.
    except PethostError as error:  # Any other code.
        print(type(error).__name__, error.message, error.detail)
```

A wrong argument the SDK sees itself, such as two members of one oneof, is Python's own
`TypeError`, `ValueError` or `OverflowError`, raised before anything is sent.

## JSON

Every message has the API's own JSON form, the one the API speaks over HTTP and
[its reference](https://pethost.dev/docs/api/) documents. `to_dict()` gives it as a dict for
`json.dumps`, and the class's `from_dict()` reads one back.

```python
import json

from pethost import Pethost, Project

with Pethost() as pethost:
    project = pethost.get_project("notes").project
    if project is not None:
        text = json.dumps(project.to_dict())  # {"project_id": "notes", ...}
        print(Project.from_dict(json.loads(text)) == project)  # True
```

A key is the API's name of a field, an enum is its value's full name, a 64-bit integer a
string, a time RFC 3339 and bytes base64. What is absent is left out, and so is a zero where
the type has no `None`: the API may write such a zero, and reads its absence as the same.

`from_dict` refuses a key that is no field of the message with a `ValueError`, as the API does,
so a misspelt key cannot pass for an absent one. A field that a newer API added is such a key
to an older version of the package. It takes what the API takes beside its own form: a key in
lowerCamelCase, a 64-bit integer as a number, an enum by its number. An enum's value that this
version of the package has no name for is its number, both ways. `dataclasses.asdict` is not
this form: it keeps a `datetime` and an enum's member as Python has them.

## Links

- [The API's reference](https://pethost.dev/docs/api/): every call, message and field.
- [The panel](https://console.pethost.dev): your machine, your projects and your API tokens.
- [pethost.dev](https://pethost.dev): what Pethost is and what it costs.

## Docker Compose hosting at one flat price

Pethost is managed hosting for Docker Compose projects. A subscription rents one virtual machine
that only your account uses. Pethost's software on it deploys your projects, gives them HTTPS
addresses, keeps their request logs and backs them up every night. You run it through your
agent or from a web panel: both show the same projects, logs and requests.

- **A machine of your own:** nobody else's projects on it. No cold starts, nothing sleeps.
  Security updates install themselves.
- **HTTPS addresses:** anything.yourname.pethost.app at once, or your own domain with one DNS
  record. Certificates renew themselves. A password page in front of the whole site: one
  sentence to your agent.
- **Deploys from GitHub:** every push deploys itself, and an earlier commit is one step back.
- **Request logs:** every request with its status and time, the busiest paths and the error
  rate, kept for 30 days.
- **Nightly backups:** encrypted, stored off the machine, kept for 14 days.
- **SSH and SFTP** into any container, and a terminal in the panel.
- **Docker Compose, as written:** a project is a Compose file, and the same file runs anywhere
  else Docker does. A database is one more service in it, at no extra cost.
- **In the EU:** your data lives on your machine, and requests to your sites go straight to
  it, never through our panel.

**Pricing.** Starter is €9.99 a month for 2 vCPU, 3 GB of memory and 30 GB of SSD. Grow is
€17.99 for 4 vCPU, 6 GB and 60 GB. Prices are without VAT. As many projects, containers and
databases as fit: nothing is metered, and nothing is billed on top. There is no free tier.
[See the plans](https://pethost.dev/#pricing).

**Who it is for.** Solo developers and early startups who host several projects, bots or small
apps and want one fixed monthly bill, and people who build with an AI agent and want it to
deploy and run what it wrote. It is not for large teams whose applications need several regions
or autoscaling: the machine is the limit.

## How Pethost compares

| If you use | The difference |
|---|---|
| [Heroku](https://pethost.dev/about/#heroku), [Render](https://pethost.dev/about/#render), [DigitalOcean App Platform](https://pethost.dev/about/#digitalocean) | There each app, worker and database is one more line on the bill. On Pethost one flat price covers the whole machine: as many projects and databases as fit, and nothing sleeps. |
| [Railway, Fly.io](https://pethost.dev/about/#railway), [Koyeb](https://pethost.dev/about/#koyeb) | There CPU, memory and traffic are metered, so the bill moves with every busy month. On Pethost the machine is the limit: nothing is metered, nothing is billed on top. |
| [Vercel, Netlify](https://pethost.dev/about/#vercel) | Made for front ends and serverless functions: a bot, a long-running worker or a database is another service with its own price. Pethost runs the front end, the back end and the database on one machine. |
| [Coolify, Dokploy](https://pethost.dev/about/#coolify), [CapRover, Dokku, Easypanel](https://pethost.dev/about/#caprover) | Self-hosted: the server is yours to rent, update, secure and back up. Pethost is the machine and the panel together, looked after for you, and agents are first-class users, not an add-on. |
| [Sliplane](https://pethost.dev/about/#sliplane) | The closest: a flat price per server. There a Compose file is converted into its own services; Pethost runs a Compose project as written. |
| [Replit](https://pethost.dev/about/#replit) | You build and publish inside Replit, with its own agent. Pethost works with the agent you already use, and one flat price covers all your apps. |
| [PythonAnywhere](https://pethost.dev/about/#pythonanywhere) | Python only, no Docker. Pethost runs anything Docker runs, in any language. |
| [A VPS you set up yourself](https://pethost.dev/about/#vps) | The server is the cheap part. You still set up the proxy, DNS, certificates, backups and updates yourself, and fix them when they break. Pethost is the server with all of that done. |

[About Pethost](https://pethost.dev/about/) has each comparison in full, with prices.

## Questions

**Which AI agents does Pethost work with?**
Almost any agent that supports skills and MCP. The ones we tested ourselves: Claude Code, Codex,
Cursor, ChatGPT, Gemini CLI, OpenClaw, Hermes and Pi.

**What can I deploy?**
Anything that runs in Docker: web apps, APIs, bots, workers, databases. No Dockerfile? With the
plugin installed, your agent knows the details and writes it for you.

**Do I need an agent?**
No. The web panel does the same, and shows the same projects, logs and requests.

**Can I use my own domain?**
Yes. One DNS record, and the certificate comes by itself.

**Is there a free tier?**
No: €9.99 rents a real machine, so nothing sleeps. Cancel any time:
[refunds and cancellation](https://pethost.dev/refunds/) has the rules.

