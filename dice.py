#!/usr/bin/env python3

# Filename: dice.py 
# Author: DMR

# This program simulates dice throws until a double 6 is thrown

import random

while True:
    dice1 = random_number = random.randint(1,6)
    dice2 = random_number = random.randint(1,6)
    total = dice1 + dice2
    print(dice1, "  ", dice2, "  ", total)
    if (dice1 == 6) and (dice2 == 6):
        break
print('Box Cars.')

