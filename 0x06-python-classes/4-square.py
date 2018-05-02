#!/usr/bin/python3
class Square:
    """ This is the square class. """
    def __init__(self, size=0):
        """ init is called to create an object. self refers to itself

        Args:
            size (int): This is the size of the square.

        Returns:
            Nothing.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ This retrieves the size.

        Args:
            None.

        Returns:
            This returns the size.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This sets the size of the square.

        Args:
            value (int): This is the value size of the square.

        Return:
            Nothing.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0 ")

        self.__size = value

    def area(self):
        """ This will guve us the area of a square.

        Args:
            None.

        Returns:
            The area.

        """
        return self.__size * self.__size
