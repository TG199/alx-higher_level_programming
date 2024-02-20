#!/usr/bin/python3
""" Write to file
"""


def write_file(filename="", text=""):
    """ writes to file and rturns the number of chars written
    Args:
        filename(textfile): file to write to
        text: data to write to file
    Returns: No of chars written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        chars_written = 0
        write_to_file = file.write(text)
        for i in range(write_to_file):
            chars_written += 1
        return chars_written
