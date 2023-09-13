#!/usr/bin/python3
""" This module is about reading from a file"""


def read_file(filename=""):
    """Opens a file in read mode and print its content
        to standard output
    Args:
        filename: Name of file to read

    Returns: Number of bytes read
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
