#!/usr/bin/python3
""" A lookup function"""


def lookup(obj):
    """
    Args:
        obj(object):
    Returns: available attributes and methids of the object
    """
    return (dir(obj))
