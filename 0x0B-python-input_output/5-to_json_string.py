#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """ This returns the JSON representation of an object (string).

    Args:
        my_obj - This is our object(string).
    """
    return json.dumps(my_obj)
