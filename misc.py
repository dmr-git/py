#!/usr/bin/env python3

# Author: DMR

import os
import sys


count = 0

def func1():
    # sample code here if parameter is passed
    print("Hello " + os.environ["USER"] + "!\n")


def set_count(c):
    global count
    count = c

def default():
    # main program goes here
    print(count)
    set_count(5)
    print(count)
    print("Bye!\n")


def main():
    os.system("clear")
    if len(sys.argv) == 2 and sys.argv[1] == "hello":
        func1()
    else:
        default()


if __name__ == "__main__":
    main()
