#!/usr/bin/python3
def number_of_lines(filename=""):
    """ This returns the number of lines of a text file.

    Args:
        filename - This is the name of the text file being tested.

    """

    number_of_lines = 0
    with open(filename) as x:
        for line in x:
            number_of_lines = number_of_lines + 1
    return number_of_lines
