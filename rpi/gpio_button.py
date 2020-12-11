#!/usr/bin/env python3

# place button input on pin10 and add a resistor inline on the power lead

import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print("Button pushed.")
    time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)

message = input("Press enter to quit.\n\n")

GPIO.cleanup()
