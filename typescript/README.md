# Pethost SDK for TypeScript and JavaScript

[Pethost](https://pethost.dev) is a small cloud for personal projects, easy to use for you and
your agent: a machine of your own that runs Docker Compose projects, at one flat price. This
package is its API as a typed client for Node 22, Bun and Deno. It reads the machine, deploys
a project, queries its logs and requests or follows them as they come, and runs commands in
its containers: the calls an agent makes, and the API's streams.

## Install

```sh
npm install pethost          # Node 22 or newer; Bun: bun add pethost
deno add jsr:@pethost/sdk    # Deno, from JSR: import from "@pethost/sdk"
```

## Get a token

In [the panel](https://console.pethost.dev), open Settings and make a token under "API
tokens". It starts with `pth_` and acts as your account, so keep it out of the code: the
program below reads it from the environment, as `PETHOST_TOKEN`.

## A first program

It reads the machine and its projects, then deploys to the project `notes` by writing one
file, `/hello.txt`.

```ts
import { Pethost, PethostError } from "pethost";

const pethost = new Pethost({ token: process.env.PETHOST_TOKEN! });

// The machine, and every project on it.
const { machine, projects } = await pethost.getMachine();
console.log(machine?.hostname);
for (const project of projects) console.log(project.projectId);

// A deploy to the project "notes": one file written, the others as they are. The call waits a
// while for the deploy to end: the operation's status says whether it did.
try {
  const { operation, project, violations } = await pethost.deployProject({
    projectId: "notes",
    files: [{ path: "/hello.txt", text: "Hello from the Pethost SDK\n" }],
  });
  for (const violation of violations) console.log(`${violation.location}: ${violation.violationMessage}`);
  if (operation) console.log(operation.status);
  if (project) console.log(project.url);
} catch (error) {
  if (!(error instanceof PethostError)) throw error;
  if (error.projectBusy) console.log(`busy with ${error.projectBusy.operationId}: try again when it ends`);
  else console.log(`${error.code}: ${error.message}`);
}
```

## Methods

A method is one call of the API. It takes the call's request and answers with its response,
both described in [the API's reference](https://pethost.dev/docs/api/) and in the comments an
editor shows. A stream answers with its responses one by one, as "Streams" below shows.

| Method | What it does | Effect |
|---|---|---|
| `getMachine` | Get the machine | Reads only |
| `runMachineAction` | Run a machine action | Destructive |
| `getProject` | Get a project | Reads only |
| `createProject` | Create a project |  |
| `deployProject` | Deploy a project | Destructive |
| `listCommits` | List a project's commits | Reads only |
| `runProjectAction` | Run a project action | Destructive |
| `getOperation` | Get an operation | Reads only |
| `queryHttpTraffic` | Query HTTP traffic | Reads only |
| `queryContainerLogs` | Query container logs | Reads only |
| `runServiceCommand` | Run a command in a service | Destructive |
| `readPath` | Read a file or directory | Reads only |
| `createTransfer` | Upload or download a file | Destructive |
| `watchOperation` | Watch an operation | Stream |
| `tailContainerLogs` | Follow container logs | Stream |
| `tailHttpTraffic` | Follow HTTP traffic | Stream |

- A key left out of a request, or `undefined`, is not sent.
- Where the API takes one of several fields, the request takes one of several keys, and two
  do not compile. A response says which one it holds.
- A time is a `Date` and a 64-bit number a `bigint`.
- A value of an enum is its name as a string. A value newer than your version of the SDK
  arrives as its number.
- Nothing retries, pages or waits on its own. To cancel a call or limit its time, pass
  `{ signal }` as the second argument.

## Streams

A stream is a method that returns what to loop over with `for await`: each response as the API
sends it, for as long as the loop runs. This program prints a project's newest log lines, then
follows them.

```ts
import { Pethost } from "pethost";

const pethost = new Pethost({ token: process.env.PETHOST_TOKEN! });

// The newest lines of the project "notes", and where a stream goes on from them without
// missing one.
const newest = await pethost.queryContainerLogs({ projectId: "notes" });
for (const line of newest.lines) console.log(line.service, line.text);

// Each later line as it is written. The loop ends when the stream fails; to stop it sooner,
// leave the loop or abort a signal given as `{ signal }`.
const request = { projectId: "notes", afterCursor: newest.tailCursor };
for await (const { line } of pethost.tailContainerLogs(request)) {
  if (line) console.log(line.service, line.text);
}
```

The call is made when the loop starts. A stream that fails throws a `PethostError` from the
loop, once, after the responses that came before it. Leaving the loop, or aborting the signal,
ends the call. The package does not call again by itself: where a response carries a cursor,
as a log line does, a new call goes on from it.

## JSON

Every message has a constant of its name that writes it as the API's own JSON and reads it
back: what the API answers and takes over HTTP, and what
[its reference](https://pethost.dev/docs/api/) documents. This program prints the machine
that way.

```ts
import { GetMachineResponse, Pethost } from "pethost";

const pethost = new Pethost({ token: process.env.PETHOST_TOKEN! });

// The machine and its projects as the API's own JSON: `apps_domain`, not `appsDomain`.
const json = GetMachineResponse.toJson(await pethost.getMachine());
const text = JSON.stringify(json, null, 2);
console.log(text);

// And back: the message again, typed as the call answered it.
const { machine } = GetMachineResponse.fromJson(JSON.parse(text));
console.log(machine?.appsDomain);
```

- The JSON has the API's names, not this package's: a field as `project_id`, a value of an
  enum with its prefix, a 64-bit number as a string, a time as RFC 3339.
- `JSON.stringify` of a message is not the API's JSON: use `toJson` first.
- `toJson` writes a message as a call sends it: no key for a zero that the API reads as
  absent, and a time to the millisecond. In those two ways a response written back may differ
  from what the API wrote.
- `fromJson` throws on a field the API does not have, as the API refuses one, and on a name of
  an enum's value newer than your version of the SDK.

## Errors

A call that fails rejects with a `PethostError`:

- `error.code` says how it failed, to branch on:
  `CANCELLED`, `UNKNOWN`, `INVALID_ARGUMENT`, `DEADLINE_EXCEEDED`, `NOT_FOUND`, `ALREADY_EXISTS`, `PERMISSION_DENIED`, `RESOURCE_EXHAUSTED`, `FAILED_PRECONDITION`, `ABORTED`, `OUT_OF_RANGE`, `UNIMPLEMENTED`, `INTERNAL`, `UNAVAILABLE`, `DATA_LOSS`, `UNAUTHENTICATED`.
  A server that could not be reached is `UNAVAILABLE`, and a call you aborted is `CANCELLED`.
- `error.message` is the server's sentence for people.
- A detail, when the server sent one, says what to do next:
  - `error.projectBusy`: Detail of an UNAVAILABLE error: an operation, or a short action, holds the project. The message says the same in words.
  - `error.projectChanged`: Detail of an ABORTED error: baseDeployId is not the current deploy: the project was deployed since you read it. Read it again (Project.deployId) and redo your change on its files.
  - `error.machineUnreachable`: Detail of an UNAVAILABLE error: the machine does not answer now, as while it restarts. Call again later.
  - `error.noMachine`: Detail of a FAILED_PRECONDITION error: the account has no machine to run projects on yet.

## Links

- [The API's reference](https://pethost.dev/docs/api/): every call, message and field.
- [The panel](https://console.pethost.dev): your machine, your projects and your API tokens.
- [pethost.dev](https://pethost.dev): what Pethost is.

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

