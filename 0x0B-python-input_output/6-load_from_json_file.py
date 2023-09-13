#!/usr/bin/python3
"""This module is about JSON file"""


def load_from_json_file(filename):
    """creates an Object from a JSON file

    Args:
        filename: name of file to write to
    Returns: An object
    """
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        python_obj = json.load(file)
        return python_obj
