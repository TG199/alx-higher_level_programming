#!/usr/bin/python3
if __nam__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        Sum = 1
        total_args = len(sys.argv) - 1
        print(f"{total_args} arguments:")
        for i in range(1, len(sys.argv)):
            if total_args > 0:
                print(f"{Sum}: {sys.argv[i]}")
                Sum += 1
