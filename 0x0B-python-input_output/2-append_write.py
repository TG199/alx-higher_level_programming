#!/usr/bin/python3
"""Write to file
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename(textfile): file to append data
        text: data to append to file

    Returns: No of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        chars_appended = 0
        append_to_file = file.write(text)

        for i in range(append_to_file):
            chars_appended += 1
        return chars_appended
