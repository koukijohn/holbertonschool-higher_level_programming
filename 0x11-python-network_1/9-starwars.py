#!/usr/bin/python3
"""
"""

import requests
import sys


if __name__ == "__main__":

    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(url)
    dictionary = r.json()
    print('Number of results: {}'.format(dictionary['count']))

    for value in dictionary['results']:
        print(value['name'])
