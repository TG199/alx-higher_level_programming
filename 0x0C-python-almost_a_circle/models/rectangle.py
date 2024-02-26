#!/usr/bin/python3
""" A Rectangle module
"""
from models.base import Base
from models.validator import int_validator


class Rectangle(Base):
    """Represents a rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes all instance and base class attributes
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int): x
            y(int): y
            id(int): id of instance
        """
        super().__init__(id)
        int_validator("width", width)
        self.__width = width
        int_validator("height", height)
        self.__height = height
        int_validator("x", x)
        self.__x = x
        int_validator("y", y)
        self.__y = y

    @property
    def width(self):
        """Gets Value of the width of rectangle
        Returns: Width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of width
        Args:
            value(int): value to set width
        """
        int_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Gets the value of height of rectangle
        Returns: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height value
        Args:
            value(int): value of height
        """
        int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ Gets the value of x
        Returns: the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the value of x
        Args:
            value: value to set x to
        """
        int_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Gets the value of y
        Returns: the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y
        Args:
            value: value to set y to
        """
        int_validator("y", value)
        self.__y = value

    def area(self):
        """ Area of the rectangle instance
        Returns: Area of rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """ Prints the representation of instance in '#'
        """
        rectangle = self.__y * "\n"
        for i in range(self.__height):
            rectangle += (" " * self.__x)
            rectangle += ("#" * self.__width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """Prints class rep
        """
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '\
            f'{self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height
            }
