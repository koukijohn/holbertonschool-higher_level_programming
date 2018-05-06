#!/usr/bin/python3

def print_square(size):
    """ This function prints a square

    Args:
        size: size is the size length of the square.

    Return:
        Nothing.
    """

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print("")
