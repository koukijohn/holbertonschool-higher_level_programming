#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        firstelem = 0, 0
    if len(tuple_a) == 1:
        firstelem = tuple_a[0], 0
    if len(tuple_a) == 2:
        firstelem = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 0:
        secondelem = 0, 0
    if len(tuple_b) == 1:
        secondelem = tuple_b[0], 0
    if len(tuple_b) == 2:
        secondelem = tuple_b[0], tuple_b[1]
    return firstelem[0] + secondelem[0], firstelem[1] + secondelem[1]
