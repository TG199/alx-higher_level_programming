#!/usr/bin/python3
"""Thsi module defines a class to JSON file"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

    Args:
        obj: class object
    Returns: Dictionary description
    """
    import json
    return json.dumps(obj.__dict__)
