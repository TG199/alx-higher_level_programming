#!/usr/bin/python3
"""This module is about a Square
"""


class Square:
    """This class defines a square
    """

    def __init__(self, size=0):
        """This method initialises the attributes 'size'
            and raises an exception if not int or >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=  0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square.

            Returns:
                int: the area of the square
        """
        return self.__size ** 2
