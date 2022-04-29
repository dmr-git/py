#!/usr/bin/env python3

ans = 2
play = input("Want to play a game? ")

while play.lower() == "y" or play.lower() == "yes":

    while True:
        guess = int(input("Please guess a number between 1 and 10: "))
        if guess == ans:
            play = input("Congratulations.  Play again? ")
            break
