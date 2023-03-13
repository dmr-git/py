#!/usr/bin/env python3

# Ask the user for their birthday in the format mm/dd/yyyy and return a string
# 'Your birth year is yyyy'
from drutils import get_date

bday = get_date("Enter your birthday in the format mm/dd/yyyy: ")

print(f'Your birth year is {bday.split("/")[2]}')
