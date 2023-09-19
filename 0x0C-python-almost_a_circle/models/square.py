#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    # The class Square is a subclass of the class Rectangle.

    def __init__(self, size, x=0, y=0, id=None):
        """
        The above function is a constructor that initializes an
        object with a given size, position, and
        id.

        Args:
          size: The size parameter represents the width and height
          of an object. It is used to determine
          the dimensions of the object.
          x: The x-coordinate of the object's position. It represents the
          horizontal position of the
        object on a 2D plane. By default, it is set to 0. Defaults to 0
          y: The `y` parameter represents the y-coordinate of the object's
          position. It determines the
        vertical position of the object on a coordinate plane. Defaults to 0
          id: The `id` parameter is an optional parameter that represents
          the unique identifier for an
        object. It is used to distinguish between different instances of
        the same class. If no `id` is
        provided, it will default to `None`.
        """
        # The line `super().__init__(size, size, x, y, id)` is calling
        # the constructor of the parent

        # class `Rectangle` and passing the arguments `size, size, x, y, id`
        # to initialize the attributes of the `Square` object.
        # This allows the `Square` class to inherit the attributes
        # and methods of the `Rectangle` class.
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        The function returns the width of an object.

        Returns:
          The width of the object.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        The function sets the width and height of an object to a given size.

        Args:
          size: The parameter "size" is the desired size for both the width
          and height of an object.
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        The function updates the attributes of an object using either
        positional arguments or keyword
        arguments.
        """
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, ["id", "size", "x", "y"][i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        The function `to_dictionary` returns a dictionary containing
        the attributes `id`, `size`, `x`,
        and `y` of an object.

        Returns:
          a dictionary with the keys 'id', 'size', 'x', and 'y'.
          The values of these keys are the
        corresponding attributes of the object that the method is called on.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        The __str__ function returns a string representation of a
        Square object, including its id,
        coordinates, and width.

        Returns:
          The `__str__` method is returning a formatted string
          that represents the Square object. It
        includes the id, x and y coordinates, and the width of the square.
        """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
