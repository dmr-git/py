#!/usr/bin/env python3

# Author: DMR

# This file demonstrates <ctrl-c> as SIGINT.  It reaps for it so the program ignores it.
# Press <ctrl-\> to send a SIGQUIT to quit.

import time
import os
import signal
import sys

def handler(ignum, time):
    print("\nI got a SIGINT, but I am not stopping")

def default():
    # main program goes here
    signal.signal(signal.SIGINT, handler)
    i = 0
    while True:
        time.sleep(.1)
        print("\r{}".format(i), end="")
        i+=1

def main():
    os.system("clear")
    if len(sys.argv) == 2 and sys.argv[1] == 'hello':
        func1()
    else:
        default()

if __name__ == '__main__':
    main()

