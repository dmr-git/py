#!/usr/bin/env python3

"""
Ask user to input 10 integers.  Print the largest odd which was entered.
If no odd numbers were entered, print a message to this affect
"""

from drutils import get_int

dict = {}
for i in range(10):
    dict[i] = get_int()

no_odd = True

for i in range(10):
    if dict[i] % 2 == 1:
        if no_odd:
            max_odd = dict[i]
            no_odd = False
        else:
            if dict[i] > max_odd:
                max_odd = dict[i]

if not no_odd:
    print(f"\nThe highest odd is {max_odd}")
else:
    print("\nNo odd number was entered.")
