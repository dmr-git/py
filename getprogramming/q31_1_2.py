#!/usr/bin/env python3


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.1415 * (self.radius**2)


circle = Circle(3)
print(circle.get_area())


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(2, 3)
print(rectangle.get_area())
print(rectangle.get_perimeter())
