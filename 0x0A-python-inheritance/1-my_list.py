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
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
