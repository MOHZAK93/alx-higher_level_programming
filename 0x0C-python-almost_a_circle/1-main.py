#!/usr/bin/python3

"""1-main"""
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.__dict__)
    r2.width = 20
    print(r2.id)
    print(r2.width)
    print(r2.__dict__)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
