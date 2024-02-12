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
        self.width = width
        self.height = height

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
        if value < 0:
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
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Gets the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Get the Perimeter of the rectangle"

        Returns:
            int: The perimeter of the rectangle
        """
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter
