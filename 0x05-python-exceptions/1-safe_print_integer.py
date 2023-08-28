#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value), end="\n")
    except ValueError:
        print("{} is not an integer".format(value), end="\n")
        return False

    return True
