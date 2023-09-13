#!/usr/bin/python3
"""This module defines a json object"""


def to_json_string(my_obj):
    """Returns JSON reps of an object

    Args:
        my_obj: object to return its json format

    Return: JSON object
    """
    import json
    json_rep = json.dumps(my_obj)
    return json_rep
