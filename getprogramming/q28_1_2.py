#!/usr/bin/python3

def invert_dict(d):
    """
    d, a dictionary
    Function returns a dictionary, with the value of the input the keys
    and the keys of the input the values. Assume the values of the input
    dictionary are immutable and unique.
    """
    ret_dict = {}
    for k in d:
        ret_dict[d[k]] = k 
    return(ret_dict)    

 # code to test
d1 = {"k1":1, "k2":2, "k3":3, "k4":4}
d2 = {"k1":"1", "k2":"2", "k3":"3", "k4":"4"}
print(invert_dict(d1))
print(invert_dict(d2))

def invert_dict_inplace(d):
    """
    d, a dictionary
    Mutate the input dictionary so that the keys become values and the 
    values become the keys. Assume that the values are immutable and unique.
    Do not return anything.
    """
    new_d = d.copy()
    d = {}
    for k in new_d.keys():
        d[new_d[k]] = k

# code to test
d1 = {"k1":1, "k2":2, "k3":3, "k4":4}
d2 = {"k1":"1", "k2":"2", "k3":"3", "k4":"4"}
d1 = invert_dict_inplace(d1)
d2 = invert_dict_inplace(d2)
print(d1)
print(d2)
