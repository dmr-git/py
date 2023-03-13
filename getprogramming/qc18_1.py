#!/usr/bin/env python3

"""
Ask for a number between 1 and 14.  If the user guesses correct
print  "You guessed right, my number was " and then print the number.  
Otherwise, keep asking for another guess
"""

my_num = "14"
guess = ""

while guess != my_num:
    guess = input("Guess a number between 1 and 14: ")

print(f"You guessed right, my number was {guess}")
