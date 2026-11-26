# Pethost for Rust

`pethost` is the Rust client of the API of [Pethost](https://pethost.dev), managed hosting for
Docker Compose projects at one flat price, as many as fit in your plan. A program does with it
what the web panel and an agent do: it reads the machine and its projects, deploys, reads logs
and HTTP traffic, runs commands in containers and moves files. Its module `pethost::sandboxes` is the
client of Pethost Agent Sandboxes, below. The crate is generated from the API's definition, so
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

## Workspaces

Each plan the account buys is a workspace: one machine of the plan's size, with its projects. A
request's `workspace` names one, by its id or its name; a client made with
`Client::new(token).with_workspace("...")` sends that in every request that names none.
With neither, a call goes to the account's only workspace, and is refused, with the workspaces
in the error, when the account has several.

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

Each is a method of [`Client`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html):
it takes the request's struct and returns the response's, or an `Error`; a stream returns its
responses one by one, as "Streams" below shows.

| Method | What it does | Effect |
|---|---|---|
| [`list_workspaces`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.list_workspaces) | List workspaces | read-only |
| [`get_machine`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.get_machine) | Get the machine | read-only |
| [`run_machine_action`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.run_machine_action) | Run a machine action | destructive |
| [`get_project`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.get_project) | Get a project | read-only |
| [`create_project`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.create_project) | Create a project |  |
| [`deploy_project`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.deploy_project) | Deploy a project | destructive |
| [`move_project`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.move_project) | Move a project to another workspace | destructive |
| [`list_commits`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.list_commits) | List a project's commits | read-only |
| [`run_project_action`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.run_project_action) | Run a project action | destructive |
| [`set_project_alerts`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.set_project_alerts) | Set a project's alerts | destructive |
| [`get_operation`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.get_operation) | Get an operation | read-only |
| [`query_http_traffic`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.query_http_traffic) | Query HTTP traffic | read-only |
| [`query_container_logs`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.query_container_logs) | Query container logs | read-only |
| [`create_database`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.create_database) | Create a database |  |
| [`link_database`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.link_database) | Link projects to a database | destructive |
| [`run_service_command`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.run_service_command) | Run a command in a service | destructive |
| [`read_path`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.read_path) | Read a file or directory | read-only |
| [`create_transfer`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.create_transfer) | Upload or download a file | destructive |
| [`watch_operation`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.watch_operation) | Watch an operation | stream |
| [`tail_container_logs`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.tail_container_logs) | Follow container logs | stream |
| [`tail_http_traffic`](https://docs.rs/pethost/0.10.1/pethost/struct.Client.html#method.tail_http_traffic) | Follow HTTP traffic | stream |

Read-only = it changes nothing. Destructive = it may delete or overwrite something. Stream =
it returns its responses one by one.

## Streams

A stream's method returns a
[`ResponseStream`](https://docs.rs/pethost/0.10.1/pethost/struct.ResponseStream.html) at
once: its `next` is each response as the API sends it, for as long as the program reads. This
program prints a project's newest log lines, then follows them. The same program is
`examples/logs.rs`.

```rust
use pethost::types::{QueryContainerLogsRequest, TailContainerLogsRequest};
use pethost::{Client, Error};

#[tokio::main]
async fn main() -> Result<(), Error> {
    // An API token from the panel's Settings, kept out of the code.
    let token = std::env::var("PETHOST_TOKEN").expect("PETHOST_TOKEN is not set");
    let pethost = Client::new(&token);

    // The newest lines of the project `notes`, and where a stream goes on from them without
    // missing one.
    let request = QueryContainerLogsRequest {
        project_id: "notes".into(),
        ..Default::default()
    };
    let newest = pethost.query_container_logs(request).await?;
    for line in &newest.lines {
        println!("{} {}", line.service, line.text);
    }

    // Each later line as it is written. The loop ends when the stream does, and `?` returns
    // the error of one that failed; to stop sooner, leave the loop.
    let request = TailContainerLogsRequest {
        project_id: "notes".into(),
        after_cursor: newest.tail_cursor,
        ..Default::default()
    };
    let mut lines = pethost.tail_container_logs(request);
    while let Some(response) = lines.next().await {
        if let Some(line) = response?.line {
            println!("{} {}", line.service, line.text);
        }
    }
    Ok(())
}
```

The call is made when the stream is first read. An error ends the stream: it comes once, as
the last item. Dropping the stream ends the call. The crate does not call again by itself:
where a response carries a cursor, as a log line does, a new call goes on from it. A
`ResponseStream` is a `Stream` of the `futures` crates too, for their combinators.

## How the API reads in Rust

- A request is a struct literal that ends in `..Default::default()`.
- A field is a plain value, and its zero means absent: such a field is not sent. An `Option`
  marks the fields where absent says something else, and every message and time.
- A oneof is an enum named after its message and itself, held in an `Option`.
- An older crate keeps reading a later API: a value it does not know reads as
  `Unrecognized(number)`, a oneof's member it does not know as `Unrecognized`, and a field it
  does not know is not seen.

## JSON

Every message and enum is `serde`'s `Serialize` and `Deserialize`, and its JSON is the API's
own, as the [API's reference](https://pethost.dev/docs/api/) shows it: the proto's field names
(`project_id`), an enum as its value's name, a 64-bit integer as a string, a time as RFC 3339,
bytes as base64. Reading refuses a field this version of the crate does not know, as the API
refuses one it does not have. With `cargo add serde_json`:

```rust
use pethost::types::{FileChange, FileChangeChange};

fn main() -> Result<(), serde_json::Error> {
    let change = FileChange {
        path: "/hello.txt".into(),
        change: Some(FileChangeChange::Text("Hello".into())),
        ..Default::default()
    };

    // The API's JSON, and the message back from it.
    let json = serde_json::to_string(&change)?;
    assert_eq!(json, r#"{"path":"/hello.txt","text":"Hello"}"#);
    assert_eq!(serde_json::from_str::<FileChange>(&json)?, change);

    // A field the API does not have is refused: here, one misspelled.
    assert!(serde_json::from_str::<FileChange>(r#"{"pth": "/hello.txt"}"#).is_err());
    Ok(())
}
```

## Errors

A failed call returns `pethost::Error`. Branch on its `code()`, one of the 16 codes of the
Connect protocol; `message()` is the API's sentence for people; `details()` is what the API
attached to say more, each a variant of `ErrorDetail`: `ProjectBusy`, `ProjectChanged`, `MachineUnreachable`, `DatabaseLinkRefusal`, `DatabaseSizeRefusal`, `NoMachine`, `PaymentOverdue`, `WorkspaceChoice`, `WorkspaceNotGranted`, `ProjectMoved`.

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

## Pethost Agent Sandboxes

Pethost Agent Sandboxes are Firecracker microVMs for AI agents, each with its own kernel
and root inside. A sandbox starts in about 0.15 s, pauses with its memory and processes while
the agent thinks, and wakes in 0.1 s at the next call: commands, files, SSH, a desktop with
Chrome, coding agents and templates.

The module `pethost::sandboxes` is its client, with the same token, read the same way as the
rest of the crate. This program is `examples/sandboxes.rs`.

```rust
use pethost::sandboxes::{types::*, Client};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let sandboxes = Client::new(&std::env::var("PETHOST_TOKEN")?);
    let id = sandboxes.create_sandbox(CreateSandboxRequest { template: "base".into(), ..Default::default() }).await?.sandbox_id;
    let hello = FileChange { path: "hello.py".into(), change: Some(FileChangeChange::Text("print(6 * 7)".into())), ..Default::default() };
    sandboxes.write_files(WriteFilesRequest { sandbox_id: id.clone(), changes: vec![hello], ..Default::default() }).await?;
    let command = sandboxes.run_command(RunCommandRequest { sandbox_id: id.clone(), command: "python3 hello.py".into(), ..Default::default() }).await?;
    println!("{:?} {}", command.exit_code, command.stdout); // Some(0) 42
    sandboxes.pause_sandbox(PauseSandboxRequest { sandbox_id: id, ..Default::default() }).await?;
    Ok(())
}
```

The calls of SandboxRuntimeService (commands, files, the desktop, links, agents) are answered by
the sandbox's own server. The client asks `connect_sandbox` where that is, keeps the answer for the
sandbox until shortly before it expires, and asks again once when a call says it no longer
holds; a sandbox made comes with its connection already. The program names no server
and holds no second token.

| Method | What it does | Effect |
|---|---|---|
| [`get_workspace`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.get_workspace) | Read the workspace | read-only |
| [`set_ssh_keys`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.set_ssh_keys) | Set the SSH keys |  |
| [`set_secret`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.set_secret) | Set a secret |  |
| [`delete_secret`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.delete_secret) | Delete a secret |  |
| [`create_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.create_sandbox) | Create a sandbox |  |
| [`get_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.get_sandbox) | Read a sandbox | read-only |
| [`list_sandboxes`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.list_sandboxes) | List sandboxes | read-only |
| [`update_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.update_sandbox) | Change a sandbox's settings | destructive |
| [`pause_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.pause_sandbox) | Pause a sandbox |  |
| [`stop_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.stop_sandbox) | Stop a sandbox | destructive |
| [`resume_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.resume_sandbox) | Resume a sandbox |  |
| [`delete_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.delete_sandbox) | Delete a sandbox | destructive |
| [`connect_sandbox`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.connect_sandbox) | Get a sandbox's address and root token |  |
| [`get_sandbox_metrics`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.get_sandbox_metrics) | Read a sandbox's metrics | read-only |
| [`list_sandbox_events`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.list_sandbox_events) | List a sandbox's events | read-only |
| [`watch_sandbox_events`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.watch_sandbox_events) | Follow a sandbox's events | stream |
| [`create_template`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.create_template) | Save a template |  |
| [`get_template`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.get_template) | Read a template version | read-only |
| [`list_templates`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.list_templates) | List templates | read-only |
| [`delete_template`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.delete_template) | Delete a template |  |
| [`list_usage`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.list_usage) | List usage | read-only |
| [`run_command`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.run_command) | Run a command | destructive |
| [`get_command`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.get_command) | Wait for a command | read-only |
| [`stop_command`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.stop_command) | Stop a command | destructive |
| [`list_commands`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.list_commands) | List running commands | read-only |
| [`watch_command`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.watch_command) | Follow a command's output | stream |
| [`read_file`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.read_file) | Read a file | read-only |
| [`list_files`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.list_files) | List files | read-only |
| [`write_files`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.write_files) | Write files | destructive |
| [`watch_files`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.watch_files) | Follow file changes | stream |
| [`control_desktop`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.control_desktop) | Use the desktop | destructive |
| [`create_link`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.create_link) | Make a link |  |
| [`prompt_agent`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.prompt_agent) | Prompt a coding agent | destructive |
| [`get_agent_turn`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.get_agent_turn) | Wait for an agent's turn | read-only |
| [`stop_agent_turn`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.stop_agent_turn) | Stop an agent's turn |  |
| [`list_conversations`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.list_conversations) | List agent conversations | read-only |
| [`watch_conversation`](https://docs.rs/pethost/0.10.1/pethost/sandboxes/struct.Client.html#method.watch_conversation) | Follow an agent conversation | stream |

Its errors are `pethost::sandboxes::Error`, with the crate's `ErrorCode` and details of its own,
`pethost::sandboxes::ErrorDetail`: `LimitReached`, `Stopped`, `UsageUnpaid`, `Restoring`, `NoCapacity`, `NameTaken`, `WorkspaceChoice`, `AgentSignIn`.

## Links

- [The crate's documentation](https://docs.rs/pethost/0.10.1): every call and message, with the API's own comments.
- [The API's reference](https://pethost.dev/docs/api/): the same API for any language.
- [The reference of Pethost Agent Sandboxes](https://pethost.dev/docs/sandboxes/api/): its API for any language.
- [The panel](https://console.pethost.dev): where a token is made.

## App Platform: Docker Compose hosting at one flat price

Pethost has two products, sold apart. The App Platform is managed hosting for Docker Compose
projects. A plan has a set size in CPU, memory and disk, at one flat price, for as many projects
as fit. Pethost's software deploys them, gives them HTTPS addresses, keeps their request logs and
backs them up every night. You run it through your agent or from a web panel: both show the same
projects, logs and requests.

- **Always on:** no cold starts, nothing sleeps, on every plan. Security updates install
  themselves.
- **HTTPS addresses:** anything.yourname.pethost.app at once, or your own domain with one DNS
  record. Certificates renew themselves. A password page in front of the whole site: one
  sentence to your agent.
- **Deploys from GitHub:** every push deploys itself, and an earlier commit is one step back.
- **Request logs:** every request with its status and time, the busiest paths and the error
  rate, kept for 30 days.
- **Nightly backups:** encrypted, stored off the machine, kept for 14 days.
- **SSH and SFTP** into any container, and a terminal in the panel.
- **Docker Compose, as written:** a project is a Compose file, and the same file runs anywhere
  else Docker does. A database is one click, Postgres, MariaDB or Valkey, with a page for
  connecting your apps, at no extra cost.
- **In the EU:** your data lives on your machine, and requests to your sites go straight to
  it, never through our panel.

**Pricing.** Starter is €9.99 a month for 2 vCPU, 3 GB of memory and 30 GB of SSD. Grow is
€17.99 for 4 vCPU, 6 GB and 60 GB. Scale is €59 for 8 vCPU, 30 GB and 200 GB. Prices are without
VAT. Whatever the plan, you can try anything: as many projects, containers and databases as
fit, nothing metered, and nothing billed on top. The App Platform has no free tier.
[See the plans](https://pethost.dev/#pricing).

**Who it is for.** Solo developers and early startups who host several projects, bots or small
apps and want one fixed monthly bill, and people who build with an AI agent and want it to
deploy and run what it wrote. It is not for large teams whose applications need several regions
or autoscaling: a plan's size is the limit.

## Agent Sandboxes: cloud VMs for AI agents, paused while they think

Pethost Agent Sandboxes are Firecracker microVMs for AI agents, each with its own kernel and root
inside. A sandbox starts in about 0.15 s, pauses with its memory and processes while the agent
thinks, and wakes in 0.1 s at the next call. Commands, files, SSH, a desktop with Chrome, Claude
Code and Codex installed, templates, an egress allow-list and API keys the sandbox never
holds. In the EU.

- **A VM per sandbox:** every sandbox is its own Firecracker microVM with its own Linux kernel,
  root inside.
- **Billed by the second** at its size's price: 2 vCPU, 4 GiB and 10 GiB for $0.018 an hour;
  each run rounded up to a second, 10 s at least.
- **Paused while idle:** it keeps its memory and processes at 30% of the running price, and the
  next call wakes it in about 0.1 s, exactly where it was. Idle longer, it stops: its disk goes to
  object storage at $0.03 per GiB a month of its own data. Nothing is deleted unless a timer says
  so.
- **Starts are free and unlimited:** creating and starting a stopped sandbox cost nothing, and no
  plan counts them; one limit against abuse, 300 a minute, is the same for every workspace.
- **API keys never enter a sandbox:** it sees a placeholder, and the egress proxy puts the key in
  HTTPS request headers, only to the hosts named. An egress allow-list by domain, wildcard, IP or
  CIDR; DNS answers only allowed names.

**Pricing.** Plans from $20 a month without VAT, the price being usage it includes; a balance
pays past it. A free trial: 7 days with $1 of usage. [See Agent Sandboxes](https://pethost.dev/sandboxes/).

**Who it is for.** Companies and developers who build on agents: AI products that run the code
their model writes, coding-agent tools, RL and eval teams, people who run Claude Code or Codex in
the cloud.

## How the App Platform compares

| If you use | The difference |
|---|---|
| [Heroku](https://pethost.dev/about/#heroku), [Render](https://pethost.dev/about/#render), [DigitalOcean App Platform](https://pethost.dev/about/#digitalocean) | There each app, worker and database is one more line on the bill. On Pethost one flat price covers everything you run: as many projects and databases as fit, and nothing sleeps. |
| [Railway, Fly.io](https://pethost.dev/about/#railway), [Koyeb](https://pethost.dev/about/#koyeb) | There CPU, memory and traffic are metered, so the bill moves with every busy month. On Pethost your plan's size is the limit: nothing is metered, nothing is billed on top. |
| [Vercel, Netlify](https://pethost.dev/about/#vercel) | Made for front ends and serverless functions: a bot, a long-running worker or a database is another service with its own price. Pethost runs the front end, the back end and the database side by side, at one flat price. |
| [Coolify, Dokploy](https://pethost.dev/about/#coolify), [CapRover, Dokku, Easypanel](https://pethost.dev/about/#caprover) | Self-hosted: the server is yours to rent, update, secure and back up. On Pethost the server and the panel come together, both looked after for you, and agents are first-class users, not an add-on. |
| [Sliplane](https://pethost.dev/about/#sliplane) | The closest: a flat price per server. There a Compose file is converted into its own services; Pethost runs a Compose project as written. |
| [Replit](https://pethost.dev/about/#replit) | You build and publish inside Replit, with its own agent. Pethost works with the agent you already use, and one flat price covers all your apps. |
| [PythonAnywhere](https://pethost.dev/about/#pythonanywhere) | Python only, no Docker. Pethost runs anything Docker runs, in any language. |
| [A VPS you set up yourself](https://pethost.dev/about/#vps) | The server is the cheap part. You still set up the proxy, DNS, certificates, backups and updates yourself, and fix them when they break. On Pethost all of that is done. |

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
No: App Platform plans start at €9.99 a month, and nothing sleeps. Agent Sandboxes has a free
trial of 7 days with $1 of usage. Cancel any time:
[refunds and cancellation](https://pethost.dev/refunds/) has the rules.

