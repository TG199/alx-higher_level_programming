#!/usr/bin/python3
""" This module defines a rectangle """


class Rectangle:
    """ Defines a Rectangle class """
    number_of_instances = 0   # Defines the number of instaces of the class
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes instances """

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

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
        rectangle_str = ""   # Defines an empty string
        for i in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Method to represent rectangle

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Method to handle deletion of an instance
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method that returns biggest rectangle

        Returns:
            biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        if rect_1.__width * rect_1.__height > rect_2.__width * rect_2.__height:
            return rect_1
        else:
            return rect_2
