#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ This creates an Object from a “JSON file”.

    Args:
        filename - This is the filename being passed.

    """

    with open(filename, encoding="UTF8") as x:
        return json.load(x)
