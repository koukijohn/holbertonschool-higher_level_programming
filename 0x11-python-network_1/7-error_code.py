#!/usr/bin/python3
"""
    This script takes in URL, sneds request to URL, and displays
    response in utf8 with requests  as our status error.
"""

import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
