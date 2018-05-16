#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ This function checks if obj is an instance of a class that inherited
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
