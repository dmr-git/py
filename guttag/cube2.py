#!/usr/bin/env python3

# Author: DMR

import os
import sys

def cube_root(num):
    ''' Use bisection search to find the cube root of a number '''
    epsilon = 0.01
    low = 0
    high = num

    guess = (high + low) / 2.0

    while (abs(guess**3 - num) >= epsilon):
        if guess**3 < num:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0


    print(f"{guess:.3f} is close to the cube root of {num:,}")  

def main():
    try: 
        os.system('clear')
        if len(sys.argv) == 2:
            argument = int(sys.argv[1])
            cube_root(argument)
        else:
            print('Usage: cube_root <int>') 
    except ValueError:
        print('Usage: cube_root <int>') 

if __name__ == '__main__':
    main()

