#!/bin/bash
# Sends JSON POST request to URL passed as first argument, and displays body.
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
