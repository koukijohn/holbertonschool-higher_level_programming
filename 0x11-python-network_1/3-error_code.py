#!/usr/bin/python3
"""
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            value = response.read().decode("utf-8")
            print(value)
    except urllib.error.HTTPError as status_error:
        print("Error code: {}".format(status_error.code))
