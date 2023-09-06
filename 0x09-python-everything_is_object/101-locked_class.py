#!/usr/bin/python3
"""This module is about a Locked class"""


class LockedClass:
    """ This class is locked """

    __slots__ = ('first_name')  # The only allowed attribute

    def __init__(self, first_name=""):
        """ Initialize instance """
        self.first_name = first_name
