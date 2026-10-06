# Pethost for Rust

`pethost` is the Rust client of the API of [Pethost](https://pethost.dev), managed hosting for
Docker Compose projects on a machine of your own. A program does with it what the web panel and
an agent do: it reads the machine and its projects, deploys, reads logs and HTTP traffic, runs
commands in containers and moves files. The crate is generated from the API's definition, so
every call, field and comment in it is the API's own.

## Install

```sh
cargo add pethost
cargo add tokio --features macros,rt-multi-thread
```

Rust 1.88 or later. Every call is `async` and runs on [Tokio](https://tokio.rs).

## A token

Every call carries an API token. Make one in the panel, [console.pethost.dev](https://console.pethost.dev):
Settings, then API tokens. The panel shows it once; it starts with `pth_`. Keep it out of the
code: the program below reads it from the environment.

## A first program

It reads the machine and its projects, then deploys to the project `notes` by writing one
file, `/hello.txt`. The same program is `examples/deploy.rs`.

```rust
use pethost::types::{DeployProjectRequest, FileChange, FileChangeChange, GetMachineRequest};
use pethost::{Client, Error};

#[tokio::main]
async fn main() -> Result<(), Error> {
    // An API token from the panel's Settings, kept out of the code.
    let token = std::env::var("PETHOST_TOKEN").expect("PETHOST_TOKEN is not set");
    let pethost = Client::new(&token);

    // The machine, and every project on it.
    let response = pethost.get_machine(GetMachineRequest::default()).await?;
    if let Some(machine) = &response.machine {
        println!("{}", machine.hostname);
    }
    for project in &response.projects {
        println!("{}", project.project_id);
    }

    // A new version of the project `notes`: one file written, the others as they are.
    let request = DeployProjectRequest {
        project_id: "notes".into(),
        files: vec![FileChange {
            path: "/hello.txt".into(),
            change: Some(FileChangeChange::Text("Hello from the Pethost SDK\n".into())),
            ..Default::default()
        }],
        ..Default::default()
    };
    let response = pethost.deploy_project(request).await?;

    // The machine refuses files it cannot run, and says what to write instead.
    for violation in &response.violations {
        println!("{}: {}", violation.location, violation.violation_message);
    }
    if let Some(operation) = &response.operation {
        println!("{:?}", operation.status);
    }
    if let Some(project) = &response.project {
        println!("{}", project.url);
    }
    Ok(())
}
```

```sh
PETHOST_TOKEN=pth_... cargo run
```

## The calls

Each is a method of [`Client`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html):
it takes the request's struct and returns the response's, or an `Error`.

| Method | What it does | Effect |
|---|---|---|
| [`get_machine`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.get_machine) | Get the machine | read-only |
| [`run_machine_action`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.run_machine_action) | Run a machine action | destructive |
| [`get_project`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.get_project) | Get a project | read-only |
| [`create_project`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.create_project) | Create a project |  |
| [`deploy_project`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.deploy_project) | Deploy a project | destructive |
| [`list_commits`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.list_commits) | List a project's commits | read-only |
| [`run_project_action`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.run_project_action) | Run a project action | destructive |
| [`get_operation`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.get_operation) | Get an operation | read-only |
| [`query_http_traffic`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.query_http_traffic) | Query HTTP traffic | read-only |
| [`query_container_logs`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.query_container_logs) | Query container logs | read-only |
| [`run_service_command`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.run_service_command) | Run a command in a service | destructive |
| [`read_path`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.read_path) | Read a file or directory | read-only |
| [`create_transfer`](https://docs.rs/pethost/0.1.0/pethost/struct.Client.html#method.create_transfer) | Upload or download a file | destructive |

Read-only = it changes nothing. Destructive = it may delete or overwrite something.

## How the API reads in Rust

- A request is a struct literal that ends in `..Default::default()`.
- A field is a plain value, and its zero means absent: such a field is not sent. An `Option`
  marks the fields where absent says something else, and every message and time.
- A oneof is an enum named after its message and itself, held in an `Option`.
- An older crate keeps reading a later API: a value it does not know reads as
  `Unrecognized(number)`, a oneof's member it does not know as `Unrecognized`, and a field it
  does not know is not seen.

## Errors

A failed call returns `pethost::Error`. Branch on its `code()`, one of the 16 codes of the
Connect protocol; `message()` is the API's sentence for people; `details()` is what the API
attached to say more, each a variant of `ErrorDetail`: `ProjectBusy`, `ProjectChanged`, `MachineUnreachable`, `NoMachine`.

```rust
use pethost::{Error, ErrorCode};

fn report(error: &Error) {
    match (error.code(), error.details()) {
        (ErrorCode::Unauthenticated, _) => eprintln!("the token is wrong or revoked"),
        (ErrorCode::Unavailable, [detail, ..]) => eprintln!("retry later: {detail:?}"),
        _ => eprintln!("{error}"),
    }
}
```

A call that never reached the API (no network, a refused connection) is `Unavailable` as well,
with the cause as the error's `source()`.

## Links

- [The crate's documentation](https://docs.rs/pethost/0.1.0): every call and message, with the API's own comments.
- [The API's reference](https://pethost.dev/docs/api/): the same API for any language.
- [The panel](https://console.pethost.dev): where a token is made.

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

