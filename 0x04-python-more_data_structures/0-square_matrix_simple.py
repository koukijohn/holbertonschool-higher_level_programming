#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for g in matrix:
        newmatrix.append([x*x for x in g])
    return newmatrix
