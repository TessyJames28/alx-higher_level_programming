#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys"""
    for x in sorted(a_dictionary):
        new_dict = a_dictionary[x]
        print(x + ":" + " " + str(new_dict))
