#!/usr/bin/env python3

# print the count of numbers between 1 and 100 which are even and divisible by
# 6 by iterating over even numbers only

ans = 0

for i in range(2,101,2):
    if (i % 6 == 0):
        ans+=1
print(f"ans = {ans}")        
