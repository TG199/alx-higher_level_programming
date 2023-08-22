#!/usr/bin/python

for i in range(0, 90):
    if i % 10 > i / 10:
        if i != 89:
            print("{:02d}, ".format(i), end="")
        else:
            print("{:02d}".format(i))
