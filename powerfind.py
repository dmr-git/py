#!/usr/bin/env python3

# Author: DMR
# Filename: powerfind.py

'''
Description:  Ask the user to enter an integer.  Print out two integers (root and pwr), such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.  If no such pair of integers exists, it should print a message to that effect.
'''    
from drutil_lib import get_int

pwrl = range(1,6)
found = False

t = get_int('Please enter an integer: ')
rootl = range(1,t+1) 

for pwr in pwrl:                 # iterate the powers
    for root in rootl:           # iterate the roots
        if root**pwr == t:
            print(root,pwr)
            found = True
            break
        elif root**pwr > t:
            break

if not (found):
    print('No such pair of integers exist.')
