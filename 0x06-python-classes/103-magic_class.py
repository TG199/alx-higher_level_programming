#!/usr/bin/python3
import math


class MagicClass:
    """A magical class that performs calculations based on radius.
    """

    def __init__(self, radius):
        """
        Initialize the MagicClass with a given radius.

        :param radius: The radius of the circle.
        :type radius: int or float
        :raises TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of a circle.

        :return: The area of the circle.
        :rtype: float
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Calculate the circumference of a circle.

        :return: The circumference of the circle.
        :rtype: float
        """
        return 2 * math.pi * self.__radius
