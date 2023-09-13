#!/usr/bin/python3
"""This module defines a JSON representation"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to write
        filename: file to write to

    Returns: No of characters written
    """
    import json
    with open(filename, 'w', encoding='utf-8') as file:
        json_rep = json.dumps(my_obj)
        content = file.write(json_rep)
        return content
