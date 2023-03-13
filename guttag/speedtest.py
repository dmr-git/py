#!/usr/bin/env python3

# Author: DMR

import os
import sys
from drutils import get_int


def func1():
    max_val = None
    while max_val != 0:
        max_val = get_int("Enter a positive integer: ")
        i = 0
        while i < max_val:
            i += 1
        print(i)


def default():
    # main program goes here
    print("Bye!\n")


def main():
    os.system("clear")
    if len(sys.argv) == 1:
        func1()
    else:
        default()


if __name__ == "__main__":
    main()
