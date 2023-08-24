#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    for i in argv:
        if i != argv[0]:
            total += int(i)

    print("{}".format(total), end="\n")
