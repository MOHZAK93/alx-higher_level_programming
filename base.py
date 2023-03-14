#!/usr/bin/python3

class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print(self.name, self.id)
