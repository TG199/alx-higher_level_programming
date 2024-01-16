#!/usr/bin/python3

for i in range(0, 100):
    if i < 10:
        
    elif i > 9 and i != 99:
        print("{}, ".format(i), end='')
    else:
        print("99")
