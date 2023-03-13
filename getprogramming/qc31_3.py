#!/usr/bin/env python3


class Door(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.open = False

    def is_open(self):
        return self.open

    def area(self):
        return self.width * self.height

    def change_state(self):
        self.open = not self.open

    def scale(self, factor):
        self.height *= factor
        self.width *= factor


square_door = Door()
square_door.change_state()
square_door.scale(3)
print(square_door.is_open())
print(square_door.area())

# explicit way of calling methods (using dot notation on the Class name)
Door.change_state(square_door)
Door.scale(square_door, 2)
print(square_door.is_open())
print(square_door.area())
