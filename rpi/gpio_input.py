#!/usr/bin/env python3

# from Paul McWhorter YouTube video lesson 6
# GPIO.PUD_DOWN makes the readings 0 until turned on
# GPIO.PUD_UP makes the readings 1 until grounded
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
in_pin = 40

# The below uses the built-in pullup/pulldown resistors on the Pi
# GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The below is for cases where I use a physical pullup/pulldown resistor
# GPIO.setup(in_pin, GPIO.IN)

try:
    while True:
        read_val = GPIO.input(in_pin)
        print(read_val)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
