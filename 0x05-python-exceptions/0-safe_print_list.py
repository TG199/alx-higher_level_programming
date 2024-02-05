#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if my_list is None:
            my_list = []

        length = 0
        for i in my_list:
            if length < x:
                print(i, end="")
                length += 1
        print()

        return length
    except Exception as e:
        print(e)
        return 0
