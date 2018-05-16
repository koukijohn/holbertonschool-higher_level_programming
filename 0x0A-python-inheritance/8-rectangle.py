#!/usr/bin/python3
""" This module imprts the BaseGeomtry class. """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ This is the rectangle class inherited from the BaseGeometry. """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
