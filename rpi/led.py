#!/usr/bin/env python3
# gpio_led.py

# LED is on pin 23, use a 270 Ohm resistor to GND
# Switch is on pin 24, use a 10K pull-down resistor to GND

import sys
import pigpio
import RPi.GPIO as GPIO
from os import system
from time import sleep
import solarized as c

# check arguments
valid_args = ['blink1', 'blink2', 'pwm']
if (len(sys.argv) == 2) and (sys.argv[1].lower() in valid_args):
    action = sys.argv[1].lower()
    system('clear')
    print('Press Ctrl-C to exit...\n')
else:
    print(c.r+'Usage: gpio_led.py [ blink1 | blink2 | pwm ]'+c.reset)
    sys.exit()

# set up gpio pins
led_pin =23
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pi = pigpio.pi()

system('clear')
print('Press Ctrl-C to exit...\n')

try:
    if (action == 'blink1'):
    # endless loop, on/off for 1 second
        while True:
            GPIO.output(led_pin, True)
            sleep(1)
            GPIO.output(led_pin, False)
            sleep(1)
    elif (action == 'blink2'):
       # remember to 'sudo pigpiod' before runnig script (to initialize the daemon)
       if not pi.connected:
            print(c.r+'Not Connected to gpio via pigpio'+c.reset)
            exit()
       while True:
            pi.write(led_pin, 1)
            sleep(1)
            pi.write(led_pin, 0)
            sleep(1)
    elif (action == 'pwm'):
        pwm_led = GPIO.PWM(led_pin, 500)  # 500 = pulses per second
        pwm_led.start(100) # 100 = percent
        while True:
            duty_s = input('Enter brightness (0 to 100): ')
            duty = int(duty_s)
            pwm_led.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    system('clear')
    print('\nCleaning up...\n')
    GPIO.cleanup()
    pi.stop()
