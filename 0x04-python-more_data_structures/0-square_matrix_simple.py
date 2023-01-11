#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for y in matrix:
        new_matrix += [list(map(lambda x: x*x, y))]
    return (new_matrix)
