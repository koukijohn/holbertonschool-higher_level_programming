#!/usr/bin/python3
""" Reads a text file (UTF8) and prints it to stdout. """


def read_file(filename=""):
    """ This reads a text file (UTF8) and prints it to stdout.

    Args:
        filename - The filename of the file that will be used.

    """
    with open(filename, mode="r", encoding="UTF8") as x:
        print(x.read(), end="")
