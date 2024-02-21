#!/usr/bin/python3
""" A student module
"""


class Student:
    """ Represents a Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes all attributes
        Args:
            first_name: First name of student
            last_name: Last name of student
            age: Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student
        Args:
            attrs: list of attributes
        """
        res = {}
        if hasattr(self, "__dict__"):
            if attrs is None:
                res = self.__dict__.copy()
            elif (isinstance(attrs, list)):
                for attr in attrs:
                    if hasattr(self, attr):
                        res[attr] = getattr(self, attr)
        return res
