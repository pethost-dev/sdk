// Command sandboxes is the README's program of Pethost Agent Sandboxes: it creates a sandbox,
// writes a Python file into it, runs it, and pauses the sandbox. Run it with an API token in
// PETHOST_TOKEN.
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/pethost-dev/sdk/go/sandboxes"
)

func main() {
	ctx := context.Background()
	client := sandboxes.NewClient(sandboxes.Config{Token: os.Getenv("PETHOST_TOKEN")})
	sandbox, err := client.CreateSandbox(ctx, &sandboxes.CreateSandboxRequest{Template: "base"})
	check(err)
	id := sandbox.SandboxID
	_, err = client.WriteFiles(ctx, &sandboxes.WriteFilesRequest{SandboxID: id, Changes: []sandboxes.FileChange{
		{Path: "hello.py", Change: sandboxes.FileChangeText("print(6 * 7)")}}})
	check(err)
	command, err := client.RunCommand(ctx, &sandboxes.RunCommandRequest{SandboxID: id, Command: "python3 hello.py"})
	check(err)
	fmt.Println(*command.ExitCode, command.Stdout) // 0 42
	_, err = client.PauseSandbox(ctx, &sandboxes.PauseSandboxRequest{SandboxID: id})
	check(err)
}

// check ends the program at an error: the call's code and message.
func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
