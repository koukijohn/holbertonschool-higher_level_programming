#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list[:]
    for x in range(len(my_list)):
        if my_list[x] == search:
            list[x] = replace
    return list
