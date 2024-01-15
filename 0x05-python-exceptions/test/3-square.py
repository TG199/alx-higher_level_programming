#!/usr/bin/python3
"""This module is about a square
"""

class Square:
    """This class defines a Square
    """
    def __init__(self, size=0):
        """this method initializes a square attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method define an area method

            Return: size of area
        """
        return self.__size ** 2
