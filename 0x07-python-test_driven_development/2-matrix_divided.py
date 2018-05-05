#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ This function divides all elments of a matrix.

    Args:
        matrix: This is the matrix.
        div: This is to divide.

    Returns:
        a new matrix.

    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    """



    newmatrix = []
    for v in matrix:
        newmatrix.append(list(map(lambda v: round(v / div, 2)))
    return newmatrix
