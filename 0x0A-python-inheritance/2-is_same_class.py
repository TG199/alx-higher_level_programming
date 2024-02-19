#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ Checks if obj is of type a_class

    Args:
        obj(object)
        a_class(class)
    Returns:
        True: if  obj is of type a_class
        False: if obj is not of type a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
