# Pethost SDKs: deploy and host Docker Compose projects from TypeScript, Python, Go and Rust

[Pethost](https://pethost.dev) is a small cloud for personal projects, easy to use for you and
your agent: a machine of your own that runs Docker Compose projects, at one flat price. These
libraries are its API as a typed client in four languages. A program does with one what the web
panel and an agent do: it reads the machine, deploys a project, queries its logs and requests,
runs commands in its containers and moves files. They are the same 13 calls an agent makes.

| Language | Install | The SDK |
|---|---|---|
| TypeScript and JavaScript | `npm install pethost`, or `deno add jsr:@pethost/sdk` | [typescript/](typescript) |
| Python | `pip install pethost` | [python/](python) |
| Go | `go get github.com/pethost-dev/sdk/go` | [go/](go) |
| Rust | `cargo add pethost` | [rust/](rust) |

Each directory's README has a first program. Every call carries an API token: make one in
[the panel](https://console.pethost.dev), in Settings under "API tokens".

**[Get a machine](https://console.pethost.dev/)** · [pethost.dev](https://pethost.dev) ·
[About Pethost](https://pethost.dev/about/) · [API reference](https://pethost.dev/docs/api/)

## Generated from the API's description

[proto/v1/panel.proto](proto/v1/panel.proto) is the API's description, the file Pethost's own
server is built from. Every SDK here is generated whole from it, with no line written by hand
per method or per message: the types, the client, the errors, and the documentation, which is
the proto's comments. An SDK has the methods marked `option (mcp_tool)`, the ones an agent has
as tools; the others serve the web panel. When the API changes, the SDKs it concerns get a new
version, tagged `<language>/v<version>`.

## Another language

The description is enough to generate a client for any language with a protobuf generator:
`proto/` is the directory its imports are read from. The API answers the
[Connect](https://connectrpc.com) protocol, gRPC and gRPC-Web at `https://console.pethost.dev`,
with the token as `Authorization: Bearer pth_…`. Without a generator, a call is a POST of JSON:
[the API reference](https://pethost.dev/docs/api/#calling) shows one.

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

