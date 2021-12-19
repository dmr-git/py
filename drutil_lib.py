#!/usr/bin/env python3

# Filename:     drutil_lib.py
# Author:       DMR
# 
# Test calls of these functions can be found in drutil_tst.py

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

def comb(n,k):
    ''' Combinations refer to the selection of n things taken k at a time without repetition,
    such that the order of selection does not matter (unlike permutations).  '''

    from math import factorial as fac
    c = ( fac(n) // ( fac(k) * fac (n-k)))
    return(c)
