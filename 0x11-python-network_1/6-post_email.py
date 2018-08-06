#!/usr/bin/python3
"""
    This python script takes in a URL and email address and sends a
    POST request to the URL and will display the body of the response.
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    r = requests.post(url, data)
    print(r.text)
