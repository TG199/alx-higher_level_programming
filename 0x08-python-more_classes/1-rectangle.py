#!/usr/bin/python3
""" This module defines a rectangle """


class Rectangle:
    """ Defines a Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initializes attributes """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ Method for retrieving width atrr"""
            return self.__width

        @width.setter
        def width(self, value):
            """Method for setting a width """
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            elif width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """Method for retrieving height attr """
            return self.__height

        @height.setter
        def height(self, value):
            """ Method for setting a height atrr """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif height < 0:
                raise ValueError("height must be >= 0")
            else:
                 self.__height = value
