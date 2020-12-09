#!/usr/bin/env python3

# Filename:     serialFromPython.py
# Author:       DMR

'''
Run serialFromPython.ino on the Arduino prior to running this programt
'''

import serial
import time

serialcomm = serial.Serial('/dev/cu.usbmodem14101',9600)
serialcomm.timeout = 1

while True:
    i = input("input (on/off): ").strip()
    i = i.lower()
    if i == 'done':
        serialcomm.write('off'.encode())
        print('finished program and turned led "off"')
        break
    serialcomm.write(i.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))

serialcomm.close()    
       
