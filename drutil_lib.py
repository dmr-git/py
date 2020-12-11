#!/usr/bin/env python3

# Filename:     drutil_lib.py
# Author:       DMR

def ctof(c):
    ''' This function converts celcius to farenheight '''
    f = (c*1.8000) + 32.0000
    return(f)

def ftoc(f):
    ''' This function converts farenheight to celcius '''
    c = (f - 32.0000) / 1.8000
    return(c)

def get_int(prompt = 'Please enter an integer: '):
    ''' This method will query the user for an integer '''
    while True:
        try:
            s = input(prompt)
            n = int(s)
            return(n)
        except ValueError:
            print('ERROR! Please enter an integer.')
