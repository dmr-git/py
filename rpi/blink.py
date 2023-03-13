#!/usr/bin/env python3

# Author: DMR

from drutil_lib import get_int
from time import sleep
from os import system
import RPi.GPIO as GPIO

# Initialize the GPIO pins
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
led_pin = 23
GPIO.setup(led_pin, GPIO.OUT)


def main():
    system("clear")
    while True:
        blink_count = get_int("How many times to blink the LED (0 to quit)? ")
        if blink_count == 0:
            break
        for i in range(blink_count):
            GPIO.output(led_pin, True)
            sleep(0.5)
            GPIO.output(led_pin, False)
            sleep(0.5)
    GPIO.cleanup()


if __name__ == "__main__":
    main()
