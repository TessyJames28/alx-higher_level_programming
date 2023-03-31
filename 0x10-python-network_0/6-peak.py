#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    finds a peak in the list
    Args:
        x for interation
        plist = a copy of the given list
    """
    plist = list_of_integers
    x = 0
    for x in range(len(plist)):
        if len(plist) == 0 or plist == []:
            return
        if x == 2:
            return max(plist)
        if x == 1 and ((plist[x] >= plist[x + 1]) and
                       (plist[x] >= plist[x - 1])):
            return plist[x]
        elif ((plist[x] >= plist[x + 1]) and (plist[x] >= plist[x - 1])):
            return plist[x]
