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

    @property
    def size(self):
        """
        Getter to retrieve size

        Args:
            self: object

        Returns: Value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter to set size

        Args:
            self: object
            value: value to assign attribute to
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Area of the square

        Args:
            self: object

        Returns: The area of the Square
        """
        return self.__size * self.__size
