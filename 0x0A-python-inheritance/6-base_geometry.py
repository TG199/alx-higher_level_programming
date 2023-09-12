#!/usr/bin/python3
"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """This class is about a Base Geometry
    """
    def area(self):
        """Raises an error as area is not implemented"""
        raise Exception("area() is not implemented")
