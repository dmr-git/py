#!/usr/bin/env python3

# Author: DMR
# Filename: printexamples.py

import solarized as c
from drutils import banner

banner("Print Format Examples", "*")

print("""Dennis says, "I'd say that rPI is fun!".""")
print("This is one line.\nThis is a second line using a \\n character.")
print("I like my Raspberry \u03c0!")
print("This is a check mark: \u2714 [\\u2714]")
print("The BEL is: \u0007 [\\u0007]")

a = 5.0 * 900
b = 3.0 * 900
print("a = {0:.4f}, b = {1:.2f}".format(a, b))
print(f"a = {a:,.2f} b = {b:,.2f}")

print("int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(1024))

# the below only works in Python 3.6 or greater
a = "hi"
b = "there"
print(f"a={a} b={b}")
print(f"{a: >10} {b: >10}")
print(f"{'dennis': >10} {'richter': >10}")
print(f"{a: <10} {b: <10}")
print(f"{'dennis': <10} {'richter': <10}")
print("a=" + a + " b=" + b)
print("a={}".format(a) + " b={}".format(b))

ln = 123456789
print(f"Long number in nice format = {ln:,}")

print(c.r + "Hello", c.b + "World\n" + c.reset)

nums = [1234.643, 754.3, 2.2, 223435454.223, 65.888]
for num in nums:
    print(f"{num:15,.2f}")

print("")
args = ['cat', 'dog', 'moose']
print(args)
print(*args)
kwargsForPrint = {'sep' : '-'}
print(*args, **kwargsForPrint)