#!/usr/bin/env python3

# Homework from Paul McWhorter YouTube video lesson 6
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
button_pin = 40
led_pin = 38

# The below uses the built-in pullup/pulldown resistors on the Pi
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        read_val = GPIO.input(button_pin)
        if read_val == 1:
            GPIO.output(led_pin, 1)
        else:
            GPIO.output(led_pin, 0)
        sleep(.1)    

except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nCleaning up....')
