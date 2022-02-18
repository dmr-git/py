#!/usr/bin/env python3

# place button input on BCM24 and a 10K resistor (pull down) to ground off same pin
# other button pin to 3.3V

from os import system
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

count = 0

system('clear')
print('Press Ctrl-C to exit...\n')

try:
    while True:
        inputValue = GPIO.input(24)
        if (inputValue == True):
            count = count + 1
            print("Button pressed " + str(count) + " times.")
            sleep(.3)
        sleep(.01)
except KeyboardInterrupt:
    system('clear')
    print('Cleaning up...\n')
    GPIO.cleanup()
