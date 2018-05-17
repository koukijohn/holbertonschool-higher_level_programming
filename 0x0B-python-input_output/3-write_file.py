#!/usr/bin/python3
def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8)
    Args:
        filename - This is the filename of the text file
        text - This is the text

    Returns:
        The number of characters written.
    """

    with open(filename, mode="w", encoding="UTF8") as x:
        return x.write(text)
