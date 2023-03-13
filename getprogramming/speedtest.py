#!/usr/bin/env python3

# time.clock() was removed in python 3.8.  use time.perf_counter instead
# time.perf_counter returns a float of the time (in fractional seconds)

import time

start = time.perf_counter()

count = 0
for i in range(10_000_000):
    count += 1

end = time.perf_counter()

print(f"\nElapsed time in seconds: {(end - start):,.6f}")
print()
