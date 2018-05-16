#!/usr/bin/python3
""" This module imprts the BaseGeomtry class. """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ This is the rectangle class inherited from the BaseGeometry. """

    def __init__(self, width, height):
        """ This instantiates our width and height and validates it. """
        self.__width = width
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """ This is the string representation of rectangle. """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ This is the area of our rectangle. """
        return (self.__width * self.__height)
