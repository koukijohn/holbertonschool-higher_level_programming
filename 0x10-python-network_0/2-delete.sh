#!/bin/bash
# Bash script that sends a DELETE request to URL passed as first argument.
curl -sX "DELETE" "$1"
