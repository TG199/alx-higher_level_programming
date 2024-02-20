#!/usr/bin/python3
""" A Geometry module """


class BaseGeometry:
    """ Represents a Geometry module """

    def area(self):
        """ Raise exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate value
        Args:
            name(str): name of value
            value(int): value number
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """ Represents a derived class rectangle """

    def __init__(self, width, height):
        """ Initialize attribute """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """String representation of the class instance.
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
