#!/usr/bin/env python3

# LED is on pin 23, use a 270 Ohm resistor to GND
# Switch is on pin 24, use a 10K pull-down resistor to GND

from os import system
import RPi.GPIO as GPIO
from time import sleep

switch_pin = 24
led_pin = 23

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)

system('clear')
print('Press Ctrl-C to exit...\n')

# pressing the switch will change the state of the LED
try:
    while True:
        GPIO.output(led_pin, 1)
        GPIO.output(led_pin, GPIO.input(switch_pin))
        sleep(.05)
except KeyboardInterrupt:
    system('clear')
    print('Cleaning up...\n')
    GPIO.cleanup()


