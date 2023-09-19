#!/usr/bin/python3

"""Rectangle class module"""


from models.base import Base


class Rectangle(Base):
    """ The Rectangle class is a subclass of the Base class."""
    
    def int_validator(self, name, value):
        """
        The function `int_validator` checks if a given value
        is an integer and meets certain conditions
        based on the name parameter.

        Args:
        name: The name parameter is a string that represents
        the name of the variable being validated. It
        can be one of the following: "width", "height", "x", or "y".
        value: The value parameter is the value that needs to be
        validated. It can be any data type, but
        the function specifically checks if it is an integer.
        """
        if type(value) is not int:
                raise TypeError(f'{name} must be an intger')
        elif name in ["width", "height"]:
                if value <= 0:
                    raise ValueError(f'{name} must be > 0')
        elif name in ["x", "y"]:
            if value < 0:
                raise ValueError(f'{name} must be >= 0')

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The function initializes an object with specified
        width, height, x and y coordinates.

        :param width: The width parameter represents the
        width of an object. It is used to define the
        width of an object in a class or function
        :param height: The height parameter represents
        the height of an object. It is used to set the
        height of the object when it is initialized
        :param x: The x-coordinate of the top-left
        corner of the object's bounding box. It represents
        the horizontal position of the object on the screen
        or canvas, defaults to 0 (optional)
        :param y: The `y` parameter represents the
        y-coordinate of the object's position. It determines
        the vertical position of the object on a coordinate
        plane, defaults to 0 (optional)
        :param id: The `id` parameter is used to assign
        a unique identifier to an object. It is an
        optional parameter and if not provided, it will
        be set to `None`
        """
        super().__init__(id)

        self.int_validator("width", width)
        self.int_validator("height", height)
        self.int_validator("x", x)
        self.int_validator("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        The function returns the width attribute of an object.
        :return: The width of the object.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        The function sets the width attribute of an object
        to the provided value, after performing type
        and value checks.

        :param width: The "width" parameter is used to set
        the width of an object. It is expected to be
        an integer value greater than zero
        """
        self.int_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """
        The function returns the height attribute of an object.
        :return: The height of the object.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        The function sets the height attribute of an object,
        but raises an error if the input is not an
        integer or if it is less than or equal to zero.

        :param height: The parameter "height" is the value
        that will be assigned to the instance
        variable "__height". It is expected to be an integer.
        If it is not an integer, a TypeError will
        be raised. If it is less than or equal to 0, a
        ValueError will be raised. Otherwise, the
        """
        self.int_validator("height", height)

        self.__height = height

    @property
    def x(self):
        """
        The function returns the value of the private
        variable __x.
        :return: The method is returning the value of
        the attribute `__x`.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        The function sets the value of a private variable __x
        to the input x, but raises a ValueError if
        x is less than 0.

        :param x: The parameter "x" is an integer value
        that represents a value to be assigned to the
        attribute "__x" of an object
        """
        
        self.int_validator("x", x)

        self.__x = x

    @property
    def y(self):
        """
        The function returns the value of the
        private variable __y.
        :return: The method is returning the value of the
        private variable `__y`.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        The function sets the value of the private attribute
        "__y" to the input parameter "y", but
        raises a ValueError if "y" is less than 0.

        :param y: The parameter "y" is a value that
        represents a coordinate or position on a vertical
        axis
        """
        ''' if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError('y must be >= 0')'''
        self.int_validator("y", y)

        self.__y = y

    def area(self):
        """
        The above function calculates the area of a rectangle.
        :return: The area of the rectangle, which is calculated
        by multiplying the width and height of
        the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        The function displays a rectangle of a given
        width and height at a specified position (x, y) on
        the screen.
        :return: nothing (None).
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        for i in range((self.y)):
            for j in range(self.x):
                print("", end="")
            print()

        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        The function updates the attributes of an
        object using either positional arguments or keyword
        arguments.
        """
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, ["id", "width", "height", "x", "y"][i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        The function `to_dictionary` returns a dictionary containing
        the attributes of an object.

        Returns:
          a dictionary with the following key-value pairs:
        - 'id': the value of self.id
        - 'width': the value of self.width
        - 'height': the value of self.height
        - 'x': the value of self.x
        - 'y': the value of self.y
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        The above function returns a string representation
        of a Rectangle object.
        :return: The `__str__` method is returning a
        string representation of a Rectangle object. The
        string includes the object's id, x and y coordinates,
        width, and height.
        """
        return f'[Rectangle]({self.id}) {self.x}/{self.y} \
            - {self.width}/{self.height}'
