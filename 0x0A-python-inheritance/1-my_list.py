#!/usr/bin/python3
""" This module is about a class inherenting from
    list
"""


class MyList(list):
    """ Sub class that inherent from list
    """
    def print_sorted(self):
        """ Prints list in sorted manner
        """
        print("{}".format(sorted(self)))
