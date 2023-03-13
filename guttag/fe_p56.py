""" The Empire State Building is 102 stories high.  A man wanted to know
    the highest floor which he could drop an egg without the egg breaking.
    Implement a method that uses at worst 7 eggs
"""


def egg_break(floor):
    if floor == 1:
        return False
    else:
        return True


eggs_used = 0

low = 1
high = 102

floor = (high - low) // 2

while True:
    if egg_break(floor):
        print(f"floor tested = {floor}")
        high = floor
        floor = ((high - low) // 2) + 1
        eggs_used += 1
    else:
        break

print(f"eggs_used = {eggs_used}")
