# Pethost for Go

The Go SDK of [Pethost](https://pethost.dev), managed hosting for Docker Compose projects: a
client of its API. With it a program does what the web panel and an agent do: it reads the
account's machine, creates and deploys projects, runs commands in their containers, and reads
their files, logs and HTTP traffic. Every type and method is generated from the API's own
definition, and their doc comments are the API's documentation.

## Install

```sh
go get github.com/pethost-dev/sdk/go@v0.1.0
```

It needs Go 1.26 or later. The package is `pethost`, which its path does not say, so an
import names it: `import pethost "github.com/pethost-dev/sdk/go"`.

## A token

Every call carries an API token of your account. Make one in the
[panel](https://console.pethost.dev), in Settings under "API tokens", and give it to the
program in its environment: the examples read `PETHOST_TOKEN`. A token starts with `pth_` and is
shown once, when it is made. A program with one can deploy to and manage your machine, and cannot
change the account.

## A first program

It reads the machine with its projects, then writes a file of the project `notes` and deploys
it. The same program is `example/main.go`.

```go
// Command example is the README's first program: it reads the account's machine and deploys a
// change to its project "notes". Run it with an API token in PETHOST_TOKEN.
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"

	pethost "github.com/pethost-dev/sdk/go"
)

func main() {
	ctx := context.Background()
	client := pethost.NewClient(pethost.Config{Token: os.Getenv("PETHOST_TOKEN")})

	// The machine and every project on it. A nil request is the empty one.
	response, err := client.GetMachine(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}
	if response.Machine != nil {
		fmt.Println(response.Machine.Hostname)
	}
	for _, project := range response.Projects {
		fmt.Println(project.ProjectID)
	}

	// A deploy: one file written over the project's own. The call waits for the deploy's end.
	deploy, err := client.DeployProject(ctx, &pethost.DeployProjectRequest{
		ProjectID: "notes",
		Files: []pethost.FileChange{
			{Path: "/hello.txt", Change: pethost.FileChangeText("Hello from the Pethost SDK\n")},
		},
	})
	if e, ok := errors.AsType[*pethost.Error](err); ok && e.ProjectBusy != nil {
		log.Fatalf("the project is busy with operation %s: try again later", e.ProjectBusy.OperationID)
	}
	if err != nil {
		log.Fatal(err)
	}

	for _, violation := range deploy.Violations {
		fmt.Println("refused:", violation.Location, violation.ViolationMessage)
	}
	if deploy.Operation != nil {
		fmt.Println(deploy.Operation.Status)
	}
	if deploy.Project != nil {
		fmt.Println(deploy.Project.URL)
	}
}
```

A request is a struct you fill in; a nil one is the empty one. A pointer says "may be absent":
set such a field with Go's `new`, as in `new(uint32(0))` for a zero that is sent. A choice of
one among several is a value of the member's type, as the file's change above.

## Methods

Each is a method of `pethost.Client` that takes a context and its request, and returns its
response or an error.

| Method | What it does | |
|---|---|---|
| `GetMachine` | Get the machine | read-only |
| `RunMachineAction` | Run a machine action | destructive |
| `GetProject` | Get a project | read-only |
| `CreateProject` | Create a project |  |
| `DeployProject` | Deploy a project | destructive |
| `ListCommits` | List a project's commits | read-only |
| `RunProjectAction` | Run a project action | destructive |
| `GetOperation` | Get an operation | read-only |
| `QueryHTTPTraffic` | Query HTTP traffic | read-only |
| `QueryContainerLogs` | Query container logs | read-only |
| `RunServiceCommand` | Run a command in a service | destructive |
| `ReadPath` | Read a file or directory | read-only |
| `CreateTransfer` | Upload or download a file | destructive |

## Errors

Every error a method returns is a `*pethost.Error`. Its `Code` says what kind of failure it
is, under the name the API's documentation uses: `pethost.CodeNotFound` prints as `NOT_FOUND`.
Its `Message` says what failed and what to do, for people. Some failures carry a detail to act
on, each a field of the error that is nil when the API sent none:
`ProjectBusy`, `ProjectChanged`, `MachineUnreachable` and `NoMachine`.

```go
response, err := client.GetMachine(ctx, nil)
if e, ok := errors.AsType[*pethost.Error](err); ok {
	switch e.Code {
	case pethost.CodeUnauthenticated:
		// The token is missing, wrong or revoked.
	case pethost.CodeUnavailable:
		// Try again later. errors.Unwrap(err) is what failed below the API, if it was not reached.
	}
}
```

A call that never reached the API is such an error too, and `errors.Is(err, context.Canceled)`
works on it.

## More

- [The API's reference](https://pethost.dev/docs/api/): every method, message and field.
- [The panel](https://console.pethost.dev): the same account in the browser.
- [The package on pkg.go.dev](https://pkg.go.dev/github.com/pethost-dev/sdk/go): every type and
  method, as `go doc github.com/pethost-dev/sdk/go` prints them.

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

