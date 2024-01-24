#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_list = []
    x = 0
    for i in range(len(my_list)):
        if my_list[i] not in unique_list:
            x += my_list[i]
            unique_list.append(i)
    return x
