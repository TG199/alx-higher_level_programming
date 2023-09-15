#!/usr/bin/python3
"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """This class is about a Base Geometry
    """
    def __init__(self, width, height):
        
        # The line `self.__width = width` is assigning the value of the `width` parameter to the
        # `__width` attribute of the object. The double underscores before the attribute name indicate
        # that it is a private attribute, meaning it should not be accessed or modified directly from
        # outside the class.
        self.__width = width
        self.__height = height
        

    def integer_validator(self, name, value):
        """Validates an integer"""

        if type(value) is not int:
            raise TypeError("{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than 0")

        self.name = name
        self.value = value
        
    def __str__(self):
        return f'[Rectangle] {self.__width} / {self.__height}'


class Rectangle(BaseGeometry):
    """subclass of base geometry. defines a rectangle"""

    def __init__(self, width, height):
        """initialises attributtes of Rectangle class"""
        super().__init__(width,height)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    
        
    def area(self):
        return self._BaseGeometry__width * self._BaseGeometry__height
    
    def __str__(self):
        return f'[Rectangle] {self.__width} / {self.__height}'

