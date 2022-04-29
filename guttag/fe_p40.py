#!/usr/bin/env python3

''' Write a program that prints the sum of the prime numbers greater than 2
    and less than 1000.  Hint use a for loop that is a prime test nested inside
    a for loop that iterates over the odd integers between 3 and 999
'''

from drutils import is_prime

sum_prime = 0

for x in range(3,1000,2):
    if is_prime(x):
        sum_prime += x

print(f'The sum of the prime numbers >2 and <1000 is {sum_prime:,}')
