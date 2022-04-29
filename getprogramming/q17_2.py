#!/usr/bin/env python3

from drutils import get_int

count = get_int()

for iter in range(count,0,-1):
    if iter > 2:
        print(f"{iter} books on Python on the shelf {iter} books on Python")
        print(f"Take one down, pass it around, {iter-1} books left.")
    elif iter == 2:    
        print(f"{iter} books on Python on the shelf {iter} books on Python")
        print(f"Take one down, pass it around, {iter-1} book left.")
    else:    
        print(f"{iter} book on Python on the shelf {iter} book on Python")
        print(f"Take one down, pass it around, no more books!")
