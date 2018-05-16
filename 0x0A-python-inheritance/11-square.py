#!/usr/bin/python3
""" This module ia about inheriting rectangle class into square class. """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ This is a class that inherits from class Rectangle.
    """
    def __init__(self, size):
        """ This instantiaties the size for the square. """
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
