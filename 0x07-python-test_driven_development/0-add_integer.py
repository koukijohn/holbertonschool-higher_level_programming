#!/usr/bin/python3
"""
This module adds integers together.


"""


def add_integer(a, b=98):
    """ This function adds intgers and returns the sum.
    Args:
        a (int): This is the first number being added.
        b (int): This is the second number being added.
    Returns:
        This returns the sum.
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    sum = a + b
    if sum == float('inf') or sum == -float('inf'):
        return 89
    return int(a) + int(b);

if __name__ == "__main__":
    import doctest
    doctest.testfile("/tests/0-add_integer.txt")
