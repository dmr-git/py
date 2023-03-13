#!/usr/bin/env python3

import random
import time

start = time.perf_counter()

cont = True
cont_list = ["Y", "YES"]

while cont:
    user_die = random.randint(1, 6)
    print(f"Your throw is {user_die}")
    computer_die = random.randint(1, 6)
    time.sleep(2)
    print(f"Computer's throw is {computer_die}")
    get_input = input("Do you want to continue playing? ")

    if cont_list.count(get_input.upper()) == 0:
        cont = False

end = time.perf_counter()

print(f"You have been playing for {(end-start):,.2f} seconds.")
