#!/usr/bin/env python3

# Filename:  arduino_style.py

# this example simulates Ardiuno style coding with a setup() section that runs
# only once and a continous loop() section.

# Declare global variables
n = 0


# Setup function
def setup():
    global n
    n = 100


# Loop
def loop():
    global n
    n = n + 1
    if (n % 2) == 0:
        print(n)


# Main
setup()
while True:
    loop()
