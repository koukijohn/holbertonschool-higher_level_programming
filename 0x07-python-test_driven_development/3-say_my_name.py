#!/usr/bin/python3
"""
This module prints ``My name is <first name> <last name>``
"""

def say_my_name(first_name, last_name=""):
    """This function checks if str or not and prints first and last name.

    Args:
        first_name: This is the first name.
        last_name: This is the last name.

    Returns:
        None.
    """

    if type(first_name) != str:
            raise TypeError("first_name must be a string")
    if type(last_name) != str:
            raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
