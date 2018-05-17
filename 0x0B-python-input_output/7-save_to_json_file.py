#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ This writes an object to a text file, using a JSON representation.

    Args:
        my_obj - This is the obj being passed.
        filename - This is the filename being passed.

    """

    with open(filename, mode="w", encoding="UTF8") as x:
        x.write(json.dumps(my_obj))
