#!/usr/bin/env python3

# genetate 10 million random numbers and time how long it takes
# time.clock() was removed in python 3.8.  use time.perf_counter instead
# time.perf_counter returns a float of the time (in fractional seconds)

import time
import random

start = time.perf_counter()

for i in range(10_000_000):
    random.randint(0,1_000_000)

end = time.perf_counter()

print(f"Elapsed time in seconds: {(end - start):,.6f}")



