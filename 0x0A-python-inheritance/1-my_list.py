#!/usr/bin/python
""" A list module """


class MyList(list):
    """ Represent a List class """

    def print_sorted(self):
        """ Print sorted list items """
        print(sorted(self))
