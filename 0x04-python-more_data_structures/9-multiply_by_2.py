#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    sum = a_dictionary.copy()
    for x in a_dictionary:
        sum[x] = sum[x] * 2
    return sum
