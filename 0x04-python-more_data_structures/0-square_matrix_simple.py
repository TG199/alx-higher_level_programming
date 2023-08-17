#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            i = i**2
            new_row.append(i)
        new_matrix.append(new_row)
    return new_matrix
