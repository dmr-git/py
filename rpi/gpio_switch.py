#!/usr/bin/env python3
#gpio_switch.py
# LED is on pin 4, use a 270 Ohm resistor to GND 
# Switch is on pin 22, use a 10K pull-down resistor to GND

import RPi.GPIO as GPIO
import time

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

# pressing the switch will change the state of the LED 
while True:
    print(GPIO.input(22)
    GPIO.output(4, True)
#    GPIO.output(4, GPIO.input(22))
    time.sleep(.05)
