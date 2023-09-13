#!/usr/bin/python3
"""This module is about appending text to a file"""


def append_write(filename="", text=""):
    """Appends text to a file and returns number of
        text appended

    Args:
        filename: Name of file
        text: text string to append

    Returns: No of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as file:

        char_appended = 0
        for char in text:
            file.write(char)
            char_appended += 1
        return char_appended

