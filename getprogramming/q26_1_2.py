#!/usr/bin/env python3

cities = "san francisco,boston,chicago,indianapolis"

# print the above string in sorted order
city_list = cities.split(",")
city_list.sort()
for city in city_list:
    print(city)


def is_permutation(list1, list2):
    """
    Function taes in 2 lists.  Return True if list1 and list2 are permutations
    of each other, False otherwise.  (every element in list1 is in list2, and
    vice versa)
    """
    ret_val = sorted(list1) == sorted(list2)
    return ret_val


print(is_permutation([1, 2, 3], [3, 1, 2]))
print(is_permutation([1, 1, 1, 2], [1, 2, 1, 1]))
print(is_permutation([1, 2, 3, 1], [1, 2, 3]))
