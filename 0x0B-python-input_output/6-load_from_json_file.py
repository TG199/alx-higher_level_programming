#!/usr/bin/python3
"""This module is about JSON file"""


def load_from_json_file(filename):
    """creates an Object from a JSON file

    Args:
        filename: name of file to write to
    Returns: An object
    """
    import json
    with open(filename, encoding='utf-8') as file:
        json_rep = json.dumps(filename)
        python_obj = json.loads(json_rep)
        return python_obj
