#!/usr/bin/env python3


def unique(in_list):
    """
    in_list, a list
    Returns a new list containing only unique elements in in_list. Do not
    mutate in_list
    """

    out_list = []

    for val in in_list:
        if val not in out_list:
            out_list.append(val)
    return out_list


def common(list1, list2):
    """
    Function does not mutate list1 or list2
    Returns True if every unique element in list1 is in list2 and if every
    unique element in list2 is in list1
    """
    list1_unique = unique(list1)
    list2_unique = unique(list2)
    return_val = True

    for val in list1_unique:
        if val not in list2_unique:
            return_val = False

    for val in list2_unique:
        if val not in list1_unique:
            return_val = False
    return return_val


print(common([1, 2, 3], [3, 1, 2]))
print(common([1, 1, 1], [1]))
print(common([1], [1, 2]))
