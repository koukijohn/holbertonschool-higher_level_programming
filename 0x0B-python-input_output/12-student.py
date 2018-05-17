#!/usr/bin/python3
class Student:
    """ This is the Stduent class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        if attributes is None:
            return self.__dict__
        else:
            dictrepr = {}
            for key, value in self.__dict__.items():
                if key in attributes:
                    dictrepr[key] = value
            return dictrepr
