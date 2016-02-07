package main

import (
	"log"

	"github.com/elos/metis"
	"github.com/elos/metis/builtin/epy"
)

func main() {
	models, err := metis.ParseGlob("./definitions/models/*/*json")
	if err != nil {
		log.Fatalf("Error parsing the moels: %s", err)
	}

	schema := metis.BuildSchema(models...)

	if err := epy.Generate(schema, "../models.py"); err != nil {
		log.Fatal(err)
	}
}
