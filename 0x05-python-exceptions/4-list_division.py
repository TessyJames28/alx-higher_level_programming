#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Write a function that divides element by element 2 lists.
    my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    list_length can be bigger than the length of both lists
    Returns a new list (length = list_length) with all divisions
    If 2 elements can’t be divided, the division result should be equal to 0
    If an element is not an integer or float:
    print: wrong type
    If the division can’t be done (/0):
    print: division by 0
    If my_list_1 or my_list_2 is too short
    print: out of range
    """
    new_list = []
    for idx in range(list_length):
        try:
            new_list.append(my_list_1[idx] / my_list_2[idx])
        except IndexError:
            print("out of range")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        finally:
            continue

    return new_list
