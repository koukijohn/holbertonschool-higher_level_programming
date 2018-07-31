#!/bin/bash
# Bash script that sends POST request to URL and displays body of response.
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
