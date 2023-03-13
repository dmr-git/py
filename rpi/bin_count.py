#!/usr/bin/env python3

# Author: DMR
"""
Set up 5 LEDs as outputs on different GPIO pins
"""

import RPi.GPIO as GPIO
from os import system
from time import sleep


def light_up(x, led):
    x_bin_lst = list(str(bin(x)[2:].zfill(5)))

    for bulb in range(5):
        if x_bin_lst[bulb] == "1":
            GPIO.output(led[bulb], True)
        else:
            GPIO.output(led[bulb], False)


def main():
    system("clear")
    GPIO.setmode(GPIO.BCM)

    led = {0: 26, 1: 19, 2: 13, 3: 6, 4: 5}

    # set the pins to Output
    for i in range(0, len(led)):
        GPIO.setup(led.get(i), GPIO.OUT)

    value = 0

    for i in range(32):
        light_up(i, led)
        sleep(1)
    GPIO.cleanup()


if __name__ == "__main__":
    main()
