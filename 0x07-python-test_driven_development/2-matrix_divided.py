#!/usr/bin/python3

"""Matrix division module"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by an integer

    Args:
        matrix: matrix to be divided
        div: matrix divider

    Returns: New matrix

    Raises:
        TypeError: Each row of the matrix must have the same size
        ZeroDivisionError: division by zero
    """
    if (
            not matrix
            or type(matrix) != list
            or any(type(row) != list for row in matrix)
            or any(
                type(elem) not in (int, float)
                for elem in [x for row in matrix for x in row]
                )
            ):
            raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x/div, 2), row)) for row in matrix]
