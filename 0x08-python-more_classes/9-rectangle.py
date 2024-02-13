#!/usr/bin/python3

"""A Rectangle module"""


class Rectangle:
    """

    Represents a Rectangle object

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        print the rectangle with the character '#'

        Returns:
            empty string: if width or height is 0
            rectangle: the '#' representation of rectangle
        """
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += (str(self.print_symbol) * self.__width) + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """
        String representation of the rectangle to be able to recreate
        a new instance by using 'eval()'

        Returns:
            str: reprensentation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print the message 'Bye rectangle...'
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Checks for biggest area of 2 rectangles

        Args:
            rect_1(Rectangle): first rectangle object
            rect_2(Rectangle): second rectangle object

        Returns: rect_1 if >= rect_2 else returns rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates new instance of Class rectangle

        Args:
            size(int): size to determine height and width of rectangle

        Returns: New instance of class rectangle
        """
        return cls(size, size)
