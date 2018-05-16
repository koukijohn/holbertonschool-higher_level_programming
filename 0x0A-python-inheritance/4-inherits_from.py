#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ This returns True if obj isinstance or class inherited from.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
