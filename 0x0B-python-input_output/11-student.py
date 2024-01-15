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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Returns: student class JSON
        """
        if attrs is not None:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)
                    }

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        re
