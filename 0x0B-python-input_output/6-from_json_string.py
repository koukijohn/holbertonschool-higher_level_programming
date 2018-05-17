#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ This returns an object represented by a JSON string.

    Args:
        my_str - This is our str being passed.

    """

    return json.loads(my_str)
