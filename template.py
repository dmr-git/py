#!/usr/bin/env python3

# Author: DMR

import os
import sys


def func1():
    # sample code here if parameter is passed
    print("Hello " + os.environ["USER"] + "!\n")


def default():
    # main program goes here
    print("Bye!\n")


def main():
    os.system("clear")
    if len(sys.argv) == 2 and sys.argv[1] == "hello":
        func1()
    else:
        default()


if __name__ == "__main__":
    main()
