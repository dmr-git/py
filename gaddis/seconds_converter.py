#!/usr/bin/env python3

# This program will vonvert an integer amount of seconst to hours, minutes and
# seconds

# get user input

seconds = int(input("Enter an amount of seconds: "))

hours = seconds // 3600

minutes = (seconds // 60) % 60

seconds = seconds % 60


print(f'Hours: {hours}\tMinutes: {minutes}\tSeconds: {seconds}')
