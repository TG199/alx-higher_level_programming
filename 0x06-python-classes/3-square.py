#!/usr/bin/python3
"""This module is about a Square
"""


class Square:
    """A class representing a Square """

    def __init__(self, size=0):
        """
        Initialize a Square instance

        Args:
            size(int): Size of the square

        Raises:
            TypeError: If size is not a int
            ValueError: if size is < 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Area of the square

        Args:
            self: object

        Returns: The area of the Square
        """
        return self.__size * self.__size
