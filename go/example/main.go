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
