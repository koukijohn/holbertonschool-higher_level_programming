#!/usr/bin/python3
def append_write(filename="", text=""):
    """ Appends a string to a text file (UTF8)
    Args:
        filename - This is the filename of the text file
        text - This is the text

    Returns:
        The number of characters written.
    """

    with open(filename, mode="a", encoding="UTF8") as x:
        return x.write(text)
