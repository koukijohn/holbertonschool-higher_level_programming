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

        self.width = width
        self.height = height

    @property
    def width(self):
        """ This retrieves the width.

        Args:
            None.

        Return:
            None.

        """
        return self.__width

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

    @property
    def height(self):
        """ This retrieves the height.

        Args:
            None.

        Return:
            None.

        """
        return self.__height

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

    def area(self):
        """ This will find the area of a rectangle.
        Args:
            None.
        Return:
            None.
        """
        return self.width * self.height

    def perimeter(self):
        """ This will find the perimeter.
        Args:
            None.
        Return:
            None.
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width + self.__width + self.__height + self.__height

    def __str__(self):
        """ This should print a rectangle with the character "#"
        Args:
                None.
        Return:
            Empty string or rectangle.
        """

        hashrectangle = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for y in range(self.__height):
            for x in range(self.__width):
                hashrectangle = hashrectangle + "#"
            if y is not (self.__height - 1):
                hashrectangle = hashrectangle + "\n"
        return hashrectangle
