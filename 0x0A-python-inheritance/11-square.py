#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The class Square is a subclass of the class Rectangle.
    """
    def __init__(self, size):
        """
        The above function is a constructor that initializes
        an object with a given size.

        :param size: The size parameter represents
        the size of the object being created. It is used to
        initialize the size attribute of the object
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        The above function calculates the area of a square.
        :return: The area of a square, which is calculated by
        multiplying the size of one side by
        itself.
        """
        return self.__size * self.__size

    def __str__(self):
        return f'[Square] {self.__size} / {self.__size}'
