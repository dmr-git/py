#!/usr/bin/env python3

# Author: DMR

# examine three integers: x,y,z  Print the largest odd.  If none are odd, print
# a message to that effect

import os
import sys

def default():
    # main program goes here
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])

    if (x >= y) and (x >= z) and (x % 2 == 1):
        print(f"{x}\n")
    elif (y >= z) and (y % 2 == 1):
        print(f"{y}\n")
    elif (z % 2 == 1):
        print(f"{z}\n")
    else:
        print("No odds.\n")

def main():
    os.system("clear")
    if len(sys.argv) != 4:
        print("Usage: high_odd <int> <int> <int>\n")
    else:
        default()

if __name__ == '__main__':
    main()

