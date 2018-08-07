#!/usr/bin/python3
"""
"""

import requests
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    github_api_auth = requests.get("https://api.github.com/user",
                                   auth=(username, password))
    dictionary = github_api_auth.json()
    try:
        print(dictionary['id'])
    except:
        print(None)
