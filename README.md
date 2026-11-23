# Pethost SDKs: App Platform and Agent Sandboxes from TypeScript, Python, Go and Rust

[Pethost](https://pethost.dev) has two products, and these libraries call both, as a typed client
in four languages.

**App Platform** is the agent-first cloud for everything you build: your agent deploys and debugs
your apps, and you see all of it in a simple panel. One flat price covers as many Docker Compose
projects as fit in your plan. A program does with its client what the web panel and an agent do:
it reads the machine, deploys a project, queries its logs and requests, runs commands in its
containers and moves files.

**Agent Sandboxes** are Firecracker microVMs for AI agents, each with its own kernel and root
inside, billed by the second. A sandbox starts in about 0.15 s, pauses with its memory and
processes while the agent thinks, and wakes in 0.1 s at the next call. A program creates
sandboxes, runs commands and coding agents in them, moves files, uses the desktop and saves
templates. The client reaches each sandbox's own server itself: a program writes no
address and no token of a sandbox's.

Both are the calls an agent makes, and the API's live streams.

| Language | Install | App Platform | Agent Sandboxes | The SDK |
|---|---|---|---|---|
| TypeScript and JavaScript | `npm install pethost`, or `deno add jsr:@pethost/sdk` | `import { Pethost } from "pethost"` | `import { Sandboxes } from "pethost/sandboxes"` | [typescript/](typescript) |
| Python | `pip install pethost` | `from pethost import Pethost` | `from pethost.sandboxes import Sandboxes` | [python/](python) |
| Go | `go get github.com/pethost-dev/sdk/go` | `github.com/pethost-dev/sdk/go` | `github.com/pethost-dev/sdk/go/sandboxes` | [go/](go) |
| Rust | `cargo add pethost` | `pethost::Client` | `pethost::sandboxes::Client` | [rust/](rust) |

Each directory's README has a first program of each. Every call carries an API token: make one in
[the panel](https://console.pethost.dev), in Settings under "API tokens".

**[Get a machine](https://console.pethost.dev/)** · [Agent Sandboxes](https://pethost.dev/sandboxes/) ·
[pethost.dev](https://pethost.dev) · [About Pethost](https://pethost.dev/about/) ·
[API reference](https://pethost.dev/docs/api/) · [Sandboxes' API reference](https://pethost.dev/docs/sandboxes/api/)

## Generated from the API's description

The API's description is two files, the ones Pethost's own servers are built from:
[proto/v1/panel.proto](proto/v1/panel.proto), App Platform's, and
[proto/v1/sandboxes.proto](proto/v1/sandboxes.proto), Agent Sandboxes'. Every SDK here is
generated whole from them, with no line written by hand per method or per message: the types,
the clients, the errors, and the documentation, which is the protos' comments. The first is an
SDK's package itself, the second its module `sandboxes`. An SDK has the methods marked
`option (mcp_tool)`, the ones an agent has as tools, and those marked `option (sdk_method)`, the
live streams among them, each read in the language's own way of iterating; the others serve the
web panel. When the API changes, the SDKs it concerns get a new version, tagged
`<language>/v<version>`.

## Another language

The description is enough to generate a client for any language with a protobuf generator:
`proto/` is the directory its imports are read from. The API answers the
[Connect](https://connectrpc.com) protocol, gRPC and gRPC-Web at `https://console.pethost.dev`,
with the token as `Authorization: Bearer pth_…`. Without a generator, a call is a POST of JSON:
[the API reference](https://pethost.dev/docs/api/#calling) shows one. Agent Sandboxes'
`SandboxService` is called there too; its `SandboxRuntimeService`, what runs inside a sandbox,
is called at the sandbox's own server, with the address and token that `ConnectSandbox` answers:
[the sandboxes' API reference](https://pethost.dev/docs/sandboxes/api/) shows both.

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

