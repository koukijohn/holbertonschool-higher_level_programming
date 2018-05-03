#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            elements = elements + 1
        except IndexError:
            pass
    print("")
    return elements
