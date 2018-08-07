#!/usr/bin/python3
"""
    This takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with letter as parameter
"""

import requests
import sys


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]

    try:
        data = {"q": q}
        r = requests.post(url, data)
        dictionary = r.json()  # This will make sure it is json formatted.
        if 'id' in dictionary and 'name' in dictionary:
            print("[{}] {}".format(dictionary['id'], dictionary['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
