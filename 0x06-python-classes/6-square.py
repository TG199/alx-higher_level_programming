#!/usr/bin/python3
"""This module is about a Square
"""


class Square:
    """A class representing a Square """

    def __init__(self, size=0, position=(0, 0)):
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

        if type(position) is not tuple or type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """
        Getter for retrieve position

        Args:
            self: object

        Args:
            self: object

        Returns: Value of position
        """
        return self.__position
    @position.setter
    def position(self, value):
        """
        Setter for position

        Args:
            self: object
            value: value to assign attribute
        """
        if type(position) is not tuple or type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Area of the square

        Args:
            self: object

        Returns: The area of the Square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints in stdout the square with the character '#'

        Args:
            self: object
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format('#'), end="")
            print()
        for i in range(self.__position[0]):
            for j in range(self.__position[1]):
                print("{}".format('-'), end="");
            print()
