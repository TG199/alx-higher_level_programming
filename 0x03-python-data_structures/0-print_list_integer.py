#!/usr/bin/python3
def print_list_integer(mylist=[]):
    for i in mylist:
        if isinstance(i, int):
            print("{}".format(i))
