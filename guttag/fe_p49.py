#!/usr/bin/env python3
""" Ask the user to enter an integer, and print 2 integers, root and pwr, such
    that 1 < pwr < 6 and root**pwr = the entered integer.  If no such pair of
    integers exist, print a message to this effect. """

from drutils import get_int

usr_int = get_int()
if usr_int < 0:
    usr_int = abs(usr_int)
    usr_int_neg = True
else:
    usr_int_neg = False

found = False

for root in range(0, usr_int):
    for pwr in range(2, 6):
        if root**pwr == usr_int:
            found = True
            break
    if found:
        break

# flip the sign on the root if the user entered a negative int and pwr is odd
if usr_int_neg and pwr % 2 == 1:
    root = -root
    usr_int = -usr_int

if found:
    print(f"{root}**{pwr} = {usr_int}")
else:
    print("No pairs found.")
