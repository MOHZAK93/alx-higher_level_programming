#!/usr/bin/python3
x, operand, num1, eq, num2 = input("Enter expression: ").split()
num1, num2 = int(num1), int(num2)
if operand == "+":
    print("x = {}".format(num2 - num1))
