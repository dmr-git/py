#!/usr/bin/env python3

class Queue(object):
    def __init__(self):
        self.queue = []
    def get_size(self):
        return(len(self.queue))
    def add_one(self, item):
        self.queue.append(item)
    def add_many(self, iten, n):
        for i in range(n):
            self.queue.append(item)
    def remove_one(self):
        self.queue.pop(0)
    def remove_many(self, n):
        for i in range(n):
            self.queue.pop(0)
    def show(self):
        for i in self.queue[::-1]:
            print("|_", i, "_|")

queue = Queue()
queue.add_one("person1")
queue.add_one("person2")
queue.add_one("person3")
queue.add_one("person4")

print(queue.get_size())
print("")
queue.show()
print("")
queue.remove_one()
queue.show()
print("")
queue.remove_many(2)
queue.show()
