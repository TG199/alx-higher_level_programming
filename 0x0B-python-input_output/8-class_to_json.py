#!/usr/bin/python3
"""Josn file
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object:
    Args:
        obj: json object
    Returns: dictionary description
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
