#!/usr/bin/python3
""" This class inherits from Base. """
from models.base import Base


class Rectangle(Base):
    """ This class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This will instantiate our attributes. """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def integer_validator(name, value):
        """ This will validate a value. """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.integer_validator("y", value)
        self.__y = value
