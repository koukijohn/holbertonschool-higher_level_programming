#!/usr/bin/python3
"""
    This is a python script that fetches https://intranet.hbtn.io/status w/
        - urllib
"""

import urllib.request


if __name__ == "__main__":

    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()
        utf8 = html.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(utf8))
