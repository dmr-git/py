#!/usr/bin/env python3

# Author: DMR

import os
import sys


def cube_root(num):
    """Find the cube root of a perfect cube"""
    ans = 0
    while ans**3 < abs(num):
        ans += 1
    if ans**3 != abs(num):
        return None
    else:
        if num < 0:
            ans = -ans
        return ans


def main():
    try:
        os.system("clear")
        if len(sys.argv) == 2:
            argument = int(sys.argv[1])
            print(f"The perfect cube root of {argument} is {cube_root(argument)}")
        else:
            print("Usage: cube_root <int>")
    except ValueError:
        print("Usage: cube_root <int>")


if __name__ == "__main__":
    main()
