#!/usr/bin/python3
"""Json function
"""
import json



def load_from_json_file(filename):
    """Convert Json object in a file to python object
    Args:
        filename: file containing json represenatation
    Returns: The python obj
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        json_file = file.read()
        obj = json.loads(json_file)
        return obj
