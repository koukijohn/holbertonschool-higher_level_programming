#!/usr/bin/python3
""" This module is holding the rectangle class. """


class Rectangle:
    """ This is the class Rectangle. """
    def __init__(self, width=0, height=0):
        """ This creates the properties.

        Args:
            width: This is the width of the rectangle.
            height: This is the height of the rectangle.

        Return:
            None.
        """

        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ This retrieves the height.

        Args:
            None.

        Return:
            None.

        """
        self.__height = height

    @height.setter
    def height(self, value):
        """ This sets the height equal to the value.

        Args:
            value: This is the value of the height to set.

        Return:
            None.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ This retrieves the width.

        Args:
            None.

        Return:
            None.

        """
        self.__width = width

    @width.setter
    def width(self, value):
        """ This sets the width equal to the value.

        Args:
            value: This is the value of the width to set.

        Return:
            None.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value