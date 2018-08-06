#!/usr/bin/python3
"""
    This python script takes in a URL and sends a request to the URL
    and will display the value of the variable 'X-Request-Id' found
    in the header of the response.
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode("ascii")

    # This will make the data into bytes.

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        value = response.read().decode("utf-8")
        print(value)
