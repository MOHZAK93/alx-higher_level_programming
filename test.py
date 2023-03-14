#!/usr/bin/python3
import random
import math


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

print(fib(3))

'''
def recur(num):
    if num <= 1:
        return 1
    else:
        result = num * recur(num - 1)
        return result

print("4! = ", recur(4))


multi = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        multi[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(multi[i][j], end=" || ")
    print()

timeTable = [[0] * 10 for i in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        timeTable[i][j] = "{}".format(i * j)

for i in range(1, 10):
    for j in range(1, 10):
        print("{}".format(timeTable[i][j]), end=", ")
    print()


fname, lname = input("Enter your full name: ").split()

employees = []

employees.append({"fName": fname, "lName": lname})

print(employees)

listCustomers = []

while True:
    customer = input("Enter Customer (Yes/No) : ")
    if customer == "y":
        name = input("Enter Customer Name : ")
        listCustomers.append(name)
        continue
    else:
        break

for i in listCustomers:
    print(i)
'''

