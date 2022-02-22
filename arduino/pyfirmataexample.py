#!/usr/bin/env python3

from pyfirmata import Arduino
from time import sleep
board = Arduino('/dev/cu.usbmodem14201')
<<<<<<< HEAD

# below line would just query the Arduino to get the firmata version
# print(board.get_firmata_version())
looptimes = input("How many times to blink the LED on the Arduino?: ")
print("Blinking " + looptimes + "times.")

for x in range(int(looptimes)):
=======
while (1):
>>>>>>> 4ddb0756def3de0f52a6018f6aa50f11a4d3a4f1
    board.digital[13].write(1)
    print("on")
    sleep(2)
    board.digital[13].write(0)
    print("off")
    sleep(1)
