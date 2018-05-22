#!/usr/bin/python3
""" This class inherits from Base. """
from models.base import Base


class Rectangle(Base):
    """ This class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This will instantiate our attributes. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    def area(self):
        """ This returns the area value of the Rectangle instance. """
        return self.width * self.height

    def display(self):
        """  Prints in stdout the Rectangle instance with the character # """

        xspaces = " " * self.x
        ynewlines = "\n" * self.y

        print(ynewlines, end="")
        for y in range(self.height):
            print(xspaces, end="")
            for x in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ This assigns an argument to each attribute. """
        attribute = ["id", "width", "height", "x", "y"]
        for element in range(len(args)):
            if args is not None:
                setattr(self, attribute[element], args[element])

        for key in attribute:
            if key in kwargs and kwargs[key] is not None:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ This returns the dictionary representation of a Rectangle. """
        attribute = ["id", "width", "height", "x", "y"]
        dictrepr = {}
        for element in attribute:
            dictrepr[element] = getattr(self, element)
        return dictrepr
