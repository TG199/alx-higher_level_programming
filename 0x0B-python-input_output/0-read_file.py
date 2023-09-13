#!/usr/bin/python3
""" This module is about reading from a file"""


def read_file(filename=""):
    """Opens a file in read mode and print its content
        to standard output
    Args:
        filename: Name of file to read

    Returns: Number of bytes read
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found")
    except IOError:
        print(f"An error occurred while reading the file '{filename}'.")
