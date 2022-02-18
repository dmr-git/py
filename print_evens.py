#!/usr/bin/env python3

# Author: DMR

import os

def setup():
    # code to run once goes here
    global n
    n = 0

def loop():
    # main loop goes here
    global n
    n = n + 1
    if ((n % 2) == 0):
        print(n)

def main():
    os.system("clear")

    setup()
    while True:
        loop()

if __name__ == '__main__':
    main()

