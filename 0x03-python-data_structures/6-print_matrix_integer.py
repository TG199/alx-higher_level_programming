#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print()
        for item in row:
            print("{:d}".format(item), end=" ")
    print()
