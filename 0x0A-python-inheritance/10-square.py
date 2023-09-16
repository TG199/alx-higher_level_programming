#!/usr/bin/python3
"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """This class is about a Base Geometry
    """

    def integer_validator(self, name, value):
        """Validates an integer"""

        if type(value) is not int:
            raise TypeError("{name} must be an integer")
        elif value <= 0:
            raise ValueError("{name} must be greater than 0")

        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """subclass of base geometry. defines a rectangle"""

    def __init__(self, width, height):
        """initialises attributtes of Rectangle class"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
        
    def area(self):
        """
        The above function calculates the area of a rectangle.
        :return: The area of the rectangle, which is calculated by multiplying the width and height of
        the rectangle.
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        The function returns a string representation of a Rectangle object, including its width and
        height.
        :return: The `__str__` method is returning a string representation of the object. In this case,
        it is returning a string that includes the class name "Rectangle" and the values of the
        `__width` and `__height` attributes of the object.
        """
        return f'[Rectangle] {self.__width} / {self.__height}'

class Square(Rectangle):
    
    def __init__(self, size):
        """
        The above function is a constructor that initializes an object with a given size.
        
        :param size: The size parameter is used to initialize the size attribute of the object. It
        represents the size of the object being created
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

        
    def area(self):
        """
        The above function calculates the area of a square.
        :return: The area of a square, which is calculated by multiplying the size of one side by
        itself.
        """
        return self.__size * self.__size
        