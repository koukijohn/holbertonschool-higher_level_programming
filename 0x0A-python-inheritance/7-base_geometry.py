#!/usr/bin/python3
class BaseGeometry:
    """ This is an empty class for a geometry module.
    """
    def area(self):
        """ This will find the area. """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ This will validate a value. """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
