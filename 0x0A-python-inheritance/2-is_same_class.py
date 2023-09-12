#!/usr/bin/python3
"""This module is about checking instance of
    an oject
"""


def is_same_class(obj, a_class):
    """ This function checks the instance of an object

    Args:
        obj: object to check
        a_class: class to check for
    Returns:
        True: if obj is an instance of specified class
        False: Otherwise
    """
    return type(obj) is a_class
