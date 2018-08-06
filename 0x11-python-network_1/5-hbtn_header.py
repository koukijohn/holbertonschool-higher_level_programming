#!/usr/bin/python3
"""
    This python script takes in a URL and sends a request to the URL
    and will display the value of the variable 'X-Request-Id' found
    in the header of the response.
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
