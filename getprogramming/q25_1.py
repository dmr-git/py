#!/usr/bin/env python3

menu = []
menu.append("pizza")
menu.append("beer")
menu.append("fries")
menu.append("wings")
menu.append("salad")
print(menu)
menu[0] = menu[-1]
menu.pop(1)
menu[3] = "pizza"
print(menu)
menu[1] = "quinoa"
menu[2] = "steak"
menu.pop()
print(menu)
