#!/usr/bin/python3
def safe_print_integer(value):
    try:
        format_str = "{:d}".format(value)
        print(format_str)
        return True
    except ValueError:
        return False
