#!/usr/bin/python3
"""This module is about writing to a file
"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename: Name of file to write 
        text: text string to write

    Returns: No of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        char_count = 0
        for char in text:
            file.write(char)
            char_count += 1

        return char_count
