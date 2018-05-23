#!/usr/bin/python3
""" This module imports the square class and inherits from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ This instantiates our attributes. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """ This gets the size. """
        return self.width

    @size.setter
    def size(self, value):
        """ This sets the size. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ This assigns an argument to each attribute. """
        attribute = ["id", "size", "x", "y"]

        for element in range(len(args)):
            if args is not None:
                setattr(self, attribute[element], args[element])

        for key in attribute:
            if key in kwargs and kwargs[key] is not None:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ This returns the dictionary representation of a Rectangle. """
        attribute = ["id", "size", "x", "y"]
        dictrepr = {}
        for element in attribute:
            dictrepr[element] = getattr(self, element)
        return dictrepr
