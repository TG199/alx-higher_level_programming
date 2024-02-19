#!/usr/bin/python3
""" A module about an object type
"""


def is_kind_of_class(obj, a_class):
    """ Checks if an obj is type of class
    Args:
        obj(object)
        a_class(class)

    Returns:
        True: if obj is an instance of a_class or an instance of a
        derived class of a_class
        """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False
