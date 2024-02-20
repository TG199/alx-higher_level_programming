#!/usr/bin/python3
import json
""" Json object
"""


def to_json_string(my_obj):
    """ JSON representation of an object (string)
    Args:
        my_obj(obj): Python obj
    Returns: Json object
    """
    return json.dumps(my_obj)
