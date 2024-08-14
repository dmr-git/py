#!/usr/bin/env python3

# Author: DMR

# This program simulates dice throws until a quadruple 4 is thrown!

import random

num_rolls = 0

while True:
    dice1 = random_number = random.randint(1, 6)
    dice2 = random_number = random.randint(1, 6)
    dice3 = random_number = random.randint(1, 6)
    dice4 = random_number = random.randint(1, 6)
    total = dice1 + dice2 + dice3 + dice4
    num_rolls = num_rolls + 1
    if (dice1 == 4) and (dice2 == 4) and (dice3 == 4) and (dice4 == 4):
        break
print(f"It took {num_rolls} rolls to roll three 4's")
