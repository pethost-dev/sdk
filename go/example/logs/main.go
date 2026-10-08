// Command logs is the README's stream: it prints the newest container logs of the project
// "notes", then each new line as it is written. Run it with an API token in PETHOST_TOKEN.
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	pethost "github.com/pethost-dev/sdk/go"
)

func main() {
	ctx := context.Background()
	client := pethost.NewClient(pethost.Config{Token: os.Getenv("PETHOST_TOKEN")})

	// The newest lines, and where a stream goes on from them without missing one.
	newest, err := client.QueryContainerLogs(ctx, &pethost.QueryContainerLogsRequest{ProjectID: "notes"})
	if err != nil {
		log.Fatal(err)
	}
	for _, line := range newest.Lines {
		fmt.Println(line.Service, line.Text)
	}

	// Each later line as it is written, until the stream fails. To stop sooner, leave the loop,
	// or cancel ctx: that is a failure too, with pethost.CodeCanceled.
	request := &pethost.TailContainerLogsRequest{ProjectID: "notes", AfterCursor: newest.TailCursor}
	for response, err := range client.TailContainerLogs(ctx, request) {
		if err != nil {
			log.Fatal(err)
		}
		if line := response.Line; line != nil {
			fmt.Println(line.Service, line.Text)
		}
	}
}
