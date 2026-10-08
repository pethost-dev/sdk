// Command json is the README's JSON: it reads a request from the API's JSON, calls the API
// with it and prints the response as the API's JSON. Run it with an API token in PETHOST_TOKEN.
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"

	pethost "github.com/pethost-dev/sdk/go"
)

func main() {
	client := pethost.NewClient(pethost.Config{Token: os.Getenv("PETHOST_TOKEN")})

	// A request from JSON. A field the API does not have is an error here.
	var request pethost.GetProjectRequest
	if err := json.Unmarshal([]byte(`{"project_id": "notes"}`), &request); err != nil {
		log.Fatal(err)
	}

	response, err := client.GetProject(context.Background(), &request)
	if err != nil {
		log.Fatal(err)
	}

	// The response as JSON: {"project": {"project_id": "notes", ...
	answer, err := json.MarshalIndent(response, "", "  ")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(answer))
}
