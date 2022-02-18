#!/usr/bin/env python3

# hook up a LED to GPIO.23

from os import system
import RPi.GPIO as GPIO

led_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)  # 500 = pulses per second
pwm_led.start(100) # 100 = percent

system('clear')
print('Press Ctrl-C to exit...\n')

try:
    while True:
        duty_s = input('Enter brightness (0 to 100): ')
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    system('clear')
    print('Cleaning up...\n')
    GPIO.cleanup()
