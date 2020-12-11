#!/usr/bin/env python3

# use a 270 Ohm resistor to ground and 5mm LED

import RPi.GPIO as GPIO
from time import sleep

led_pin = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:

    # endless loop, on/off for 1 second
    while True:
        GPIO.output(led_pin, True)
        sleep(1)
        GPIO.output(led_pin, False)
        sleep(1)

except KeyboardInterrupt:
    print('\nCleaning up...\n')
    GPIO.cleanup()

