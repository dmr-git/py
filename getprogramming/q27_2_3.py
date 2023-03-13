#!/usr/bin/python3


def replace(d, v, e):
    """
    d, a dictionary
    v, a value to be replaced
    e, the new value
    This function mutates the dictionary and dows not return anything
    """
    for key in d.keys():
        if d[key] == v:
            d[key] = e


# code to test the function
d1 = {1: 2, 3: 4, 4: 2}
d2 = {1: 2, 3: 1, 4: 2}
replace(d1, 2, 7)
replace(d2, 1, 2)
print(d1)
print(d2)


def invert(d):
    """
    d, a dictionary
    This finction inverts the keys to values (as a list) and the values to keys.
    Returns a new dictionary (d_inv)
    """
    d_inv = {}
    l_inv_uk = []
    l_values = list(d.values())
    l_keys = list(d.keys())

    # create a list (l_inv_uk) to be the keys for the return dictionary
    for val in l_values:
        if val not in l_inv_uk:
            l_inv_uk.append(val)

    # create the return dictionary with blank lists as value
    for key in l_inv_uk:
        d_inv[key] = []

    # populate the values in the return dictionary
    for val in l_keys:
        item = d[val]
        temp = d_inv[item]
        temp.append(val)
        d_inv[item] = temp
    return d_inv


def invert2(d):
    d_inv = {}
    for k in d:
        v = d[k]
        if v not in d_inv:
            d_inv[v] = [k]
        else:
            d_inv[v].append(k)
    return d_inv


# code to test the function
d1 = {1: 2, 3: 4, 5: 6}
d2 = {1: 2, 2: 1, 3: 3}
d3 = {1: 1, 3: 1, 5: 1}
print(invert2(d1))
print(invert2(d2))
print(invert2(d3))
