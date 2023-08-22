#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[-1]
    last_digit = int(last_digit)
    print("{}".format(last_digit), end="")
    return (last_digit);

