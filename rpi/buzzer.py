#!/usr/bin/env python3
# gpio_led.py

# LED is on pin 23, use a 270 Ohm resistor to GND
# Switch is on pin 24, use a 10K pull-down resistor to GND

import sys
from os import system
import RPi.GPIO as GPIO
from time import sleep

# set up gpio pins
buzzer_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

system("clear")
print("Press Ctrl-C to exit...\n")

try:
    buzzer = GPIO.PWM(buzzer_pin, 440)  # set frequency to 440 (A)
    buzzer.start(100)  # set dutycycle to 100
    while True:
        freq_s = input("Enter frequency (0 to 1000): ")
        freq = int(freq_s)
        buzzer.ChangeFrequency(freq)
except KeyboardInterrupt:
    system("clear")
    print("\nCleaning up...\n")
    buzzer.stop()
    GPIO.cleanup()
