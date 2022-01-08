#!/usr/bin/env python3

# Filename:     drutil_tst.py 
# Author:       DMR

import sys
import drutil_lib

def main():
    '''
    This is the main function.  It will be used to call the various examples.
    '''
    print(f"Number of combinations of 5 out of 52 objects = {drutil_lib.comb(52,5):,}")
    

if __name__ == '__main__':
    main()

