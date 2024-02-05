#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        if not my_list:
            my_list = []

        count = 0
        for i in my_list:
            if count < x:
                if isinstance(i, int):
                    print("{:d}".format(i), end="")
                    count += 1
                pass
        print()
        return count
    except Exception as e:
        print(e)
