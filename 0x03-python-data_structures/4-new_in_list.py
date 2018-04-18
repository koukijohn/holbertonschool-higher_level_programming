#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    if idx < len(my_list):
        replacement = my_list[:]
        replacement[idx] = element
        return replacement
