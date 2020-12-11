#!/usr/bin/env python3

# connect the Parallax PIR motion sensor to pin 4 and an LED to pin 16

#motion.py

from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(4)
led = LED(16)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()
