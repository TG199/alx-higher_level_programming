#!/usr/bin/env py
from sys import argv

if __name__ == "__main__":
    len_of_args = len(argv) - 1

    print("{} argument{}:".format(len_of_args, "s" if len_of_args != 1 else ""))

    for i in range(1, len_of_args + 1):
        print("{}: {}".format(i, argv[i]))
