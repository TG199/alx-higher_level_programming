#!/usr/bin/python3
"""Integer validator module"""


def int_validator(name, value):
    """
    The function `int_validator` checks if a given value
    is an integer and meets certain conditions
    based on the name parameter.

    Args:
    name: The name parameter is a string that represents
    the name of the variable being validated. It
    can be one of the following: "width", "height", "x", or "y".
    value: The value parameter is the value that needs to be
    validated. It can be any data type, but
    the function specifically checks if it is an integer.
    """
    if type(value) is not int:
        raise TypeError(f'{name} must be an integer')
    if name in ["width", "height"]:
        if value <= 0:
            raise ValueError(f'{name} must be > 0')
    if name in ["x", "y"]:
        if value < 0:
            raise ValueError(f'{name} must be >= 0')
