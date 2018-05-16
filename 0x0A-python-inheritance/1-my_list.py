#!/usr/bin/python3
""" This module is about printing the sorted self. """


class MyList(list):
    """ This is a class that inherits from list.
    """
    def print_sorted(self):
        """ This prints the list, but sorted in ascending order.
        """
        print(sorted(self))
