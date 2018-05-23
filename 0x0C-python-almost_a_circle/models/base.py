#!/usr/bin/python3
""" This module holds the Base class. """
import json


class Base:
    """ This is the class Base. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This init's the id. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        with open("{}.json".format(cls.__name__), "w",
                  encoding="UTF8") as file:
            list = []
            if list_objs is None:
                file.write(Base.to_json_string([]))
            else:
                for obj in list_objs:
                    list.append(obj.to_dictionary())
                file.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string. """
        if json_string is None or json_string is "":
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set. """
        if cls.__name__ == "Square":
            x = cls(8)
        if cls.__name__ == "Rectangle":
            x = cls(8, 8)
        x.update(**dictionary)
        return x

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances. """
        list = []
        try:
            with open("{}.json".format(cls.__name__), "r",
                      encoding="UTF8") as x:
                list = cls.from_json_string(x.read())
            for attributes in range(len(list)):
                list[attributes] = cls.create(**list[attributes])
            return list
        except:
            return list
