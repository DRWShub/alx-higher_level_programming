#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
curl "$@" -s | grep -H "Content-Type: application/json" | grep -d "$(cat "$2"@)" "$1@"
