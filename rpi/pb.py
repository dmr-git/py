#!/usr/bin/env python3
# LED is on pin 23, use a 270 Ohm resistor to GND
# pressing the switch will change the state of the LED
# Switch is on pin 24, use a 10K pull-down resistor to GND

import sys
import RPi.GPIO as GPIO
import solarized as c
from os import system
from time import sleep

# check arguments
valid_args = ['hold', 'toggle', 'count']
if (len(sys.argv) == 2) and (sys.argv[1].lower() in valid_args):
    action = sys.argv[1].lower()
    system('clear')
    print('Press Ctrl-C to exit...\n')
else:
    print(c.r+'Usage: gpio_pb.py [ hold | toggle | count ]'+c.reset)
    sys.exit()

# set up gpio pins
switch_pin = 24
led_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)
GPIO.output(led_pin, 0)

# main program
try:
    if (action == "hold"): # holding PB down will keep the LED lit, releasing PB turns it off
        while True:
            GPIO.output(led_pin, GPIO.input(switch_pin))
            sleep(.05)
    elif (action == "toggle"): # pressing the PB will toggle the LED on/off
        led_next_state = 1
        while True:
            if (GPIO.input(switch_pin) == 1):
                GPIO.output(led_pin, led_next_state)
                led_next_state = not led_next_state
                sleep(.3)
    elif (action == "count"):  # display count of clicks to stdout
        count = 0
        while True:
            inputValue = GPIO.input(switch_pin)
            if (inputValue == True):
                count = count + 1
                print("Button pressed " + str(count) + " times.")
                sleep(.3)
except KeyboardInterrupt:
    system('clear')
    print('Cleaning up...\n')
    GPIO.cleanup()
