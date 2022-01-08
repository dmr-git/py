#!/usr/bin/env python3

# Filename:     sig_handler.py
# Author:       DMR

import signal, time

def handler(signum, time):
    print("\nI got a SIGINT, but I am not stopping")

def main():
    signal.signal(signal.SIGINT, handler)
    i = 0
    while True:
        time.sleep(.1)
        print("\r{}".format(i), end="")
        i += 1

if __name__ == '__main__':
    main()

