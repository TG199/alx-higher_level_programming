#!/usr/bin/python3
"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """This class is about a Base Geometry
    """
    def area(self):
        """Raises an error as area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("name> must be greater than 0")

        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """subclass of base geometry. defines a rectangle"""

    def __init__(self, width, height):
        """initialises attributtes of Rectangle class"""

        BaseGeometry.__init__(self)
        self.__height = height
        self.__width = width
        self.integer_validator("width", width)
        self.integer_validator("height", height)
