#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    Sum = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            Sum += int(arg)
    print(Sum)
