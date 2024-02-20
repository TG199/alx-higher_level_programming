#!/usr/bin/python3
"""Represents a json object
"""
import json


def save_to_json_file(my_obj, filename):
    """ Save object to json file
    Args:
        my_obj(object)
        filename(json file): file to save json representation
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
