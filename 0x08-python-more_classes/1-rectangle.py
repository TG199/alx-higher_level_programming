#!/usr/bin/python3

"""A Rectangle module"""


class Rectangle:
    """

    Represents a Rectangle object

    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle

        Returns:
            int : the size of the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width

        Args:
            value(int): value to set as width size
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
            int: the size of the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value(int): value to set as height size
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
