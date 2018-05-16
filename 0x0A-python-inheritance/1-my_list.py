#!/usr/bin/python3
class MyList(list):
    """ Ths is a class that inherits from list.
    """
    def print_sorted(self):
        """ This prints the list, but sorted in ascending order.
        """
        print(sorted(self))
