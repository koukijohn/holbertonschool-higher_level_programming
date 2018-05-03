#!/usr/bin/python3
def add_integer(a, b=98):
    """ This function adds intgers and returns the sum.

    Args:
        a (int): This is the first number being added.
        b (int): This is the second number being added.

    Returns:
        This returns the sum.

    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
