#!/usr/bin/env python3

import sys

n = 0
sum = 0.0

if len(sys.argv) == 2:
    iters = int(sys.argv[1])
else:
    iters = 1000

while n < iters:
    sum = sum + (1/2**n)
    n = n + 1

print("{0:.70f}".format(sum))    



