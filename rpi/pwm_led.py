#!/usr/bin/env python3

# hook up a LED to GPIO.25

import RPi.GPIO as GPIO

led_pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)  # 500 = pulses per second
pwm_led.start(100) # 100 = percent

try:
    while True:
        duty_s = input('Enter brightness (0 to 100): ')
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    print('\nCleaning up...')
    GPIO.cleanup()
