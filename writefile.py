#!/usr/bin/env python3

# Filename: write_file.py
# Author: DMR

from datetime import datetime
from time import sleep
import random
from pathlib import Path

# this way works, but need to remember to do the flush() and close()

log = open("log.txt", "w")

for i in range(5):
    now = str(datetime.now())
    data = random.randint(0, 1024)
    log.write(now + " " + str(data) + "\n")
    print(".")
    sleep(0.9)

log.flush()
log.close()

# this is the preferred way to open a file

with open("foo.txt", "w") as foo_bar:
    foo_bar.write("This is the preferred method to write to a file.\n")
    foo_bar.write("'with open() as xx' automatically flushes and closes.")

# use the pathlib module and / to create paths that are cross platform
# refer p.19 of "Beyond the Basic Stuff with Python"
# can pass a Path object to any function oin the Python standard library
# that expects a filename

file2 = Path.home() / "code" / "py" / "foobar.txt"

with open(file2, "w") as foo_bar:
    foo_bar.write("This is an alternate way to form a path\n")
