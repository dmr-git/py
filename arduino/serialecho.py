#!/usr/bin/env python3

import serial

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)
serialFromArduino.flushInput()

while True:
    # if (serialFromArduino.inWaiting() > 0):
    #     input = serialFromArduino.read(1)
    #    # print(ord(input))
    #    print(str(ord(input)) + " = the ASCII character " + str(input) )
    input = serialFromArduino.readline()
    inputAsInteger = int(input)
    print(inputAsInteger * 10)
