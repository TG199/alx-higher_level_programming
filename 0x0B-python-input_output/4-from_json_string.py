#!/usr/bin/python3
"""This module defines a JSON object"""


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: JSON string

    Returns: Python object
    """
    import json
    python_obj = json.loads(my_str)
    return python_obj
