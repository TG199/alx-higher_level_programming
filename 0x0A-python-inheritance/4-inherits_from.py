#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ Returns true if object is an instance of a class

    Args:
    obj: object
    a_class: type class

    Returns:
            True if obj is an instance of a_class
            False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
