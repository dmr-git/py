#!/usr/bin/env python3

# Author: DMR

import os
import sys


def cube_root(num):
    """Use guess and check to find the cube root of a number"""
    guess = 0.0
    epsilon = 0.1
    increment = 0.0001

    while (abs(guess**3 - num) >= epsilon) and guess <= num:
        guess += increment

    if abs(guess**3 - num) >= epsilon:
        print(f"Failed on cube root of {num}")
    else:
        print(f"{guess:.3f} is close to the cube root of {num:,}")


def main():
    try:
        os.system("clear")
        if len(sys.argv) == 2:
            argument = int(sys.argv[1])
            cube_root(argument)
        else:
            print("Usage: cube_root <int>")
    except ValueError:
        print("Usage: cube_root <int>")


if __name__ == "__main__":
    main()
