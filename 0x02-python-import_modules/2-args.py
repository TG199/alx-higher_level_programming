#!/usr/bin/env py
from sys import argv

if __name__ == "__main__":
    i = len(argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument".format(i))
    else:
        print("{} arguments:".format(i))

    if i > 0:
        i = 0
        for arg in argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
