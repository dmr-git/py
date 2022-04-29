#!/usr/bin/env python3

# Simulate flipping a coin 100 times and print results

import random

class Coin(object):
    def __init__(self):
        self.sides = ["H", "T"]
    def flip(self):
        return(random.choice(self.sides))

coin = Coin()

flips = 1000
heads = 0
tails = 0

for i in range(flips):
    if coin.flip() == "H":
        heads += 1
    else:
        tails += 1

print(f"In {flips} coin flips there were {heads} heads {tails} tails.")

