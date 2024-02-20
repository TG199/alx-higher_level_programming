#!/usr/bin/python3
"""Json object
"""
import json


def from_json_string(my_str):
    """ Deserialize a Json obj
    Args:
        my_str(object): Python object
    Returns: Python data structure obj
    """
    return json.loads(my_str)
