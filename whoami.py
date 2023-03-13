#! /usr/bin/env python3

import os

foo = dict(os.environ)

for key in foo:
    print(f"{key} = {foo[key]}")

print("Output written to out.txt")

with open("out.txt", "w") as out_file:
    for key in foo:
        out_file.write(f"{key} = {foo[key]}\n")
