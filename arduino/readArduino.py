#!/usr/bin/env python3

import serial, time
ser = serial.Serial('/dev/ttyACM0',9600)
n = 0

while (True):
    n = n + 1
    message = ser.readline()
    print(message + " " + str(n))
    time.sleep(.5)
