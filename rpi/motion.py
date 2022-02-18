#!/usr/bin/env python3
# motion.py

# this script used the gpiozero library
# connect the Parallax PIR motion sensor to pin 17 and an LED to pin 23

from os import system
from gpiozero import MotionSensor, LED
from signal import pause                # waits until signal is received

system('clear')
print('Press Ctrl-C to exit...\n')

led_pin = 23
pir_pin = 17

led = LED(led_pin)
pir = MotionSensor(pir_pin)

pir.when_motion = led.on
pir.when_no_motion = led.off

try:
    pause()
except KeyboardInterrupt:
    system('clear')
    print('Cleaning up...\n')

