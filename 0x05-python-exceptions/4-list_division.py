#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:

        for i in range(list_length):
            try:
                n_1 = my_list_1[i]
                n_2 = my_list_2[i]
                if not isinstance(n_1, (int, float)):
                    print("Wrong type")
                    new_list.append(0)
                elif not isinstance(n_2, (int, float)):
                    print("Wrong type")
                    new_list.append(0)
                elif n_2 == 0:
                    print("division by 0")
                    new_list.append(0)
                else:
                    new_list.append(n_1 / n_2)
            except IndexError:
                print("Out of range")
                new_list.append(0)
    finally:
        return new_list
