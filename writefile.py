#!/usr/bin/env python3

# Filename: write_file.py
# Author: DMR

from datetime import datetime
from time import sleep
import random

log = open("log.txt","w")

for i in range(5):
    now = str(datetime.now())
    data = random.randint(0, 1024)
    log.write(now + " " + str(data) + "\n")
    print(".")
    sleep(.9)

log.flush()
log.close()

