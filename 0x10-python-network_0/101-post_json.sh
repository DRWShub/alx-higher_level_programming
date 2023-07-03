#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
curl "$@" -sH "Content-Type: application/json" | grep -d "$(cat "$2")" "$1"
