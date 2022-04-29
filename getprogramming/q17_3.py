#!/usr/bin/env python3

str = input("Enter names separated by a single space: ")

#solve the easy way
names = str.split()
for name in names:
    print(f"Hi {name.title()}")

# the hard way

while True:
    space_pos = str.find(" ")

    if space_pos == -1:
        name = str
        print(f"Hi {name}")
        break

    name = str[0:space_pos]
    print(f"Hi {name}")
    str = str[space_pos+1:]
