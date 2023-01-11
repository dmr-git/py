#!/usr/bin/env python3

# Homework from Paul McWhorter YouTube video lesson 9

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
button_up = 36
button_down = 40
led_pin = 38

# The below uses the built-in pullup/pulldown resistors on the Pi
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

# set up the frequency (how many cycles per second)
myPWM = GPIO.PWM(led_pin, 100)

try:
    duty_cycle = 0
    myPWM.start(duty_cycle)

    while True:
        read_up = GPIO.input(button_up)
        if read_up == 1 and duty_cycle < 100:
            duty_cycle += 12.5
            myPWM.ChangeDutyCycle(duty_cycle)
            sleep(.5)
           
        read_down = GPIO.input(button_down)
        if read_down == 1 and duty_cycle > 0:
            duty_cycle -= 12.5
            myPWM.ChangeDutyCycle(duty_cycle)
            sleep(.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nCleaning up....')
