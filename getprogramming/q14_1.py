#!/usr/bin/env python3

from drutils import get_int

while True:
    int1 = get_int()

    if int1 == 99:
        break

    int2 = get_int()

    if int1 < int2:
        print("first integer is less than second integer")
    elif int1 > int2:
        print("first integer is greater than second integer")
    else:
        print("the numbers are equal")
