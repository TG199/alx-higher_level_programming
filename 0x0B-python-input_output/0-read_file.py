#!/usr/bin/python3
"""Reads a text
"""


def read_file(filename=""):
    """Reads content of a file
    Args:
        filename(textfile)
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
