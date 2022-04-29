#!/usr/bin/env python3

name = 'Dennis M. Richter'
age = 61 #not a lie
height = 72 # inches
weight = 184 # pounds
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Lets talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age} and {height} and {weight} I get {total}.")

metric_height = height * 2.54
metric_weight = weight * .45359237
print(f"He's {metric_height} centimeters tall.")
print(f"He's {metric_weight:,.2f} kilograms heavy.")

