#!/usr/bin/env python3

from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(19)

while True:
    #    buzzer.on()
    #    sleep(.1)
    #    buzzer.off()
    #    sleep(1)
    buzzer.beep(0.1, 1, None, False)
