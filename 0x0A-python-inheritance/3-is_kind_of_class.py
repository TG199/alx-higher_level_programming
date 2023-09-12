#!/usr/bin/python3
"""This module checks object instances
"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance of a_class
        else false
    """
    return isinstance(obj, a_class)
