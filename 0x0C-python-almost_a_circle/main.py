#!/usr/bin/python3

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def talk(self):
        print(f"Hi there, I can talk")

    def walk(self):
        print(f"Hi there, I can walk")

    def __str__(self):
        return f"This person is called {self.__name}"
if __name__ == "__main__":

    P1 = Person("Zak", 29)
    print(P1._Person__name)
    print(P1.__dict__)
