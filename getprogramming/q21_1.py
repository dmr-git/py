#!/usr/bin/env python3


def calculate_total(price, percent):
    return price + (price * percent / 100)


print(calculate_total(20, 15))

my_price = 78.55
my_tip = 20

new_total = round(calculate_total(my_price, my_tip), 2)
print(f"New total: {new_total}")
