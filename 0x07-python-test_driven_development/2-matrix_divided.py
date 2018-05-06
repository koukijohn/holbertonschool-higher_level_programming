#!/usr/bin/python3
"""
This module divides the matrix by div.
"""


def matrix_divided(matrix, div):
    """ This function divides all elments of a matrix.

    Args:
        matrix: This is the matrix.
        div: This is to divide.

    Returns:
        a new matrix.

    """


    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([])
        for elements in matrix[row]:
            new_matrix[row].append(round((elements / div), 2))
    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
