#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        arg1 = 0
        arg2 = 0
    elif len_a == 1:
        arg1 = tuple_a[0]
        arg2 = 0
    else:
        arg1 = tuple_a[0]
        arg2 = tuple_a[1]

    if len_b == 0:
        secon_arg1 = 0
        secon_arg2 = 0
    elif len_b == 1:
        secon_arg1 = tuple_b[0]
        secon_arg2 = 0
    else:
        secon_arg1 = tuple_b[0]
        secon_arg2 = tuple_b[1]
    new_tuple = (arg1 + secon_arg1, arg2 + secon_arg2)
    return new_tuple
