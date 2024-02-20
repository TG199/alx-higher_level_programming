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
