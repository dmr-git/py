#!/usr/bin/env python3

# Q10.1 from page 87 of "Get programming Learn to code with PYTHON

word = "echo"
t = ()
count = 3

reps = len(word)

while reps > 0:
    t = t + (word[-reps:],)*count
    reps = reps - 1

print(t)
