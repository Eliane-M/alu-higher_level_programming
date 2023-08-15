#!/usr/bin/python3
"""
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix elements must be integers or floats otherwise raise a type error
    each row of the matrix must be the same size
    div must be a number
    div can't be 0
    raise a zerodivisionerroe if div == 0
    """
    if not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix) or \
        not all(isinstance(element, int) or isinstance(element, float):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
