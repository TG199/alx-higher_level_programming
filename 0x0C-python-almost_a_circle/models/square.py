#!/usr/bin/python3
""" A Square module
"""
from models.rectangle import Rectangle
from models.validator import int_validator


class Square(Rectangle):
    """Represents a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        int_validator("width", value)
        self.width = value
        int_validator("height", value)
        self.height = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            }

        

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'



