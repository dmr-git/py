#!/usr/bin/env python3

class Circle(object):
    def __init__(self):
        self.radius = 0
    def change_radius(self, radius):
        self.radius = radius
    def get_radius(self):
        return(self.radius)

class Stack(object):
    def __init__(self):
        self.stack = []
    def get_stack_elements(self):
        return (self.stack.copy())
    def add_one(self, item):
        self.stack.append(item)
    def add_many(self, item, n):
        for i in range(n):
            self.stack.append(item)
    def add_list(self, lst):
        for i in lst:
            self.stack.append(lst)
    def remove_one(self):
        self.stack.pop()
    def remove_many(self):
        for i in range(n):
            self.stack.pop()
    def size(self):
        return(len(self.stack))
    def prettyprint(self):
        for thing in self.stack[::-1]:
            print("|_", thing, "_|")
            
# create a stack of pancakes            
pancakes = Stack()
pancakes.add_one("blueberry")
pancakes.add_many("chocolate", 4)
print(pancakes.size())
pancakes.remove_one()
print(pancakes.size())
pancakes.prettyprint()

# create a stack of 6 different circle
circles = Stack()
one_circle = Circle()
one_circle.change_radius(2)
circles.add_one(one_circle)

for i in range(5):
    one_circle = Circle()
    one_circle.change_radius(1)
    circles.add_one(one_circle)
print(circles.size())
circles.prettyprint()

# create a stack of circles (one radius, and 5 of the same with radius 1
circles = Stack()
one_circle = Circle()
one_circle.change_radius(2)
circles.add_one(one_circle)

one_circle = Circle()
one_circle.change_radius(1)
circles.add_many(one_circle, 5)
print(circles.size())
circles.prettyprint()
