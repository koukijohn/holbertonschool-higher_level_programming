#!/usr/bin/python3
"""
    This will find a peak in a lost of unsorted integers.
    Peak: when it's neigbors are smaller than it.
"""


def find_peak(list_of_integers):
    """
        This function will find our peak.
    """
    if list_of_integers is None:
        return None
    if len(list_of_integers) == 0:
        return None
    # getting our midpoint
    midpoint = len(list_of_integers) / 2
    midpoint = int(midpoint)
    # This is comparing the middle element with its neigbours
    try:
        if (list_of_integers[midpoint - 1] <= list_of_integers[midpoint]) and
        (list_of_integers[midpoint + 1] <= list_of_integers[midpoint]):
            return list_of_integers[midpoint]
    except:
        if (list_of_integers[midpoint - 1] < list_of_integers[midpoint]):
            return list_of_integers[midpoint]

    # if left neighbor greater than midpoint, then left half has a peak elem
    if (list_of_integers[midpoint - 1] > list_of_integers[midpoint]):
        return find_peak(list_of_integers[:midpoint])
    else:
        # if right neighbor greater than midpoint, then right half has peak
        return find_peak(list_of_integers[midpoint:])
