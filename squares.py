#!/usr/bin/env python3

# Filename:     squares.py
# Author:       DMR

# remember to use 'chmod u+x filename.py' to make the script executable

squares = []

for x in range(1,11):
    squares.append(x**2)
print(squares)    

squares2 = [value**2 for value in range(1,11)]
print(squares2)

for x in range(1,21):
    print(x)

ll = [x for x in range(1,1_000_001)]

print(f"ll starts at: {ll[0]}")
print(f"ll starts at: {min(ll)}")
print(f"ll ends at: {ll[-1]}")
print(f"ll starts at: {max(ll)}")
print(f"ll starts at: {sum(ll)}")

odds = [x for x in range(1,20,2)]
for odd in odds:
    print(odd)

threes = [x for x in range(3,31,3)]
for x in threes:
    print(x)
    
