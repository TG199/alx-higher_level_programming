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

    def to_json(self):
        """ retrieves a dictionary representation of a Student
        """
        res = {}
        if hasattr(self, "__dict__"):
            res = self.__dict__.copy()
        return res
