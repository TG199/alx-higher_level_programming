#!/usr/bin/python3

def no_c(my_string):
    new_string = list()
    for i in my_string:
        if i in "cC":
            continue
        else:
            new_string.append(i)
    return new_string
