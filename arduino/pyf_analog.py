#!/usr/bin/env python3

# hook a pot to the arduino A0 pin

from pyfirmata import Arduino
import pyfirmata
from time import sleep

port = "/dev/cu.usbmodem14201"  # when running from my Mac
board = Arduino(port)

pin = board.get_pin("a:0:i")

it = pyfirmata.util.Iterator(board)
it.start()

while True:
    analog_value = pin.read()
    print(analog_value)
    sleep(0.1)
