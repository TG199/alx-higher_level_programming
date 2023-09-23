#!/usr/bin/python3

"""Rectangle class module"""


from models.base import Base


class Rectangle(Base):
    """ The Rectangle class is a subclass of the Base class."""

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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
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
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

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

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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

        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')
        ''' if self.width == 0 or self.height == 0:
            print("")
            return

        for i in range((self.y)):
            for j in range(self.x):
                print("", end="")
            print()

        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()'''

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
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh
