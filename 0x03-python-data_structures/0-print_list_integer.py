#!/usr/bin/env py
def print_list_integer(mylist=[]):
    for i in mylist:
        if isinstance(i, int):
            print("{}".format(i))

lists = ['Kele', 1, 3, 'Nasa', 5]

print_list_integer(lists)
