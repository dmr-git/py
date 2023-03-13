#!/usr/bin/env python3

# Homework from Paul McWhorter YouTube video lesson 9

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
button_up = 21
button_down = 16
led_pin = 20

# The below uses the built-in pullup/pulldown resistors on the Pi
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(led_pin, GPIO.OUT)


def button_released_callback(channel):
    global duty_cycle
    print(f"Button {channel} was released.")
    if channel == 21 and duty_cycle < 100:
        duty_cycle += 12.5
        myPWM.ChangeDutyCycle(duty_cycle)
    if channel == 16 and duty_cycle > 0:
        duty_cycle -= 12.5
        myPWM.ChangeDutyCycle(duty_cycle)


GPIO.add_event_detect(
    button_up, GPIO.RISING, callback=button_released_callback, bouncetime=50
)
GPIO.add_event_detect(
    button_down, GPIO.RISING, callback=button_released_callback, bouncetime=50
)

# set up the frequency (how many cycles per second)
myPWM = GPIO.PWM(led_pin, 100)

try:
    duty_cycle = 0
    myPWM.start(duty_cycle)

    while True:
        sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nCleaning up....")
