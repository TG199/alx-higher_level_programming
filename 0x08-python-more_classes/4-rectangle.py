#!/usr/bin/python3
""" This module defines a rectangle """


class Rectangle:
    """ Defines a Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initializes instances """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Method for retrieving width atrr

        Returns:
            width of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method for setting a width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method for retrieving height attr

        Returns:
            height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method for setting a height atrr

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height < 0


        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to get area of Rectangle
        Returns:
            area: width * height
        """
        return self.width * self.height

    def perimeter(self):
        """Method to get the perimeter of Rectangle

        Returns:
            perimeter: 2 * (width + height):
                if width and height is not 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Method to represent rectangle as #

        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Method to represent rectangle

        """
        return f"Rectangle({self.__width}, {self.__height})"
