#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [[i**2 for i in row] for row in new_matrix]
    return new_matrix
