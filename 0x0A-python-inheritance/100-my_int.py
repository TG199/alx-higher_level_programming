#!/usr/bin/python3
"""This module defines a rebel class"""


class MyInt(int):

    """Rebel class"""
    def __eq__(self, other):
        # Override the equality operator (==) to behave like !=
        return super().__ne__(other)

    def __ne__(self, other):
        # Override the inequality operator (!=) to behave like ==
        return super().__eq__(other)
