#!/usr/bin/env python3

# Author: DMR

import os
import sys

def cat():
    print('Meow')

def default():
    print('Hello '+ os.environ['USER'] + '!\n')

def main():
    os.system("clear")
    if len(sys.argv) == 2 and sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__':
    main()

