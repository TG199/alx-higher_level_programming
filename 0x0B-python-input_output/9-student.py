#!/usr/bin/python3
"""This module is about student class """


class Student:
    """Defines a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize class attributes

        Args:
            first_name: firstname attribute
            last_name: Last_name attribute
            age: age attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns: student class JSON
        """
        return self.__dict__
