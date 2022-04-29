#!/usr/bin/env python3

# Filename:     drutils.py
# Author:       DMR
# 
# Test calls of these functions can be found in drutil_tst.py
'''
Library of useful utilities.
'''

def ctof(c):
    ''' Converts celcius to farenheight '''
    f = (c*1.8000) + 32.0000
    return(f)

def ftoc(f):
    ''' Converts farenheight to celcius '''
    c = (f - 32.0000) / 1.8000
    return(c)

def get_date(prompt = 'Please enter a date in mm/dd/yyyy format: '):
    ''' Query for a date in mm/dd/yyyy format '''
    from datetime import datetime
    while True:
        input_date = input(prompt)
        try:
            month, day, year = input_date.split('/')
            datetime(int(year), int(month), int(day))
            return(input_date)
        except ValueError:
            print("Invalid entry.  Enter mm/dd/yyyy")

def get_int(prompt = 'Please enter an integer: '):
    ''' Query for an integer '''
    while True:
        try:
            s = input(prompt)
            n = int(s)
            return(n)
        except ValueError:
            print('ERROR! Please enter an integer.')

def is_prime(num):
    ''' Return True if num is prime, False if it is not '''
    if num > 1:
        for i in range(3, int(num/2)+1,2):
            if (num % i) == 0:
                return(False)
        else:
            return(True)

    else:
        return(False)

def comb(n,k):
    ''' Combinations refer to the selection of n things taken k at a time without
        repetition, such that the order of selection does not matter
        (unlike permutations) '''
    from math import factorial as fac
    c = ( fac(n) // ( fac(k) * fac (n-k)))
    return(c)

def right_justify(string, width=70):
    ''' Return the passed string right justified of length specified.  Default to 70. '''
    msg = string.strip()
    pad_count = width - len(msg)
    msg = " " * pad_count + msg
    return(msg)

def hypotunuse(a,b):
    ''' Pythagorean Theorm (a**2 + b**2 = c**2).  Solve for c '''
    from math import sqrt
    return (sqrt(a**2 + b**2))

def fact(n):
    ''' Return factiorial on n using a recursive function call '''
    if (n == 1):
        return 1
    else:
        return (n * fact(n-1))

def read_text(filename):
    ''' filename: name of file to read. Returns a string containing the
        contents of the file. '''
    in_file = open(filename, 'r')
    contents = in_file.read()
    return(contents[0:-1])

def find_words(text):
    ''' retuen a list of words from an input string '''
    from string import punctuation
    # replace newlines with space
    text = text.replace("\n", " ")
    # strip out special punctuation characters
    for char in punctuation:
        text = text.replace(char, "")
    words = text.split(" ")
    return(words)

def word_count(words):
    ''' Return a dictionary with the frequency of each word in a list of words.
    '''
    freq_dict = {}

    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return(freq_dict)

def frequencies(filename):
    '''  returns a dictionary with the word count frequency '''
    ret_str = read_text(filename)
    lst = find_words(ret_str)
    wc = word_count(lst)
    return(wc)

