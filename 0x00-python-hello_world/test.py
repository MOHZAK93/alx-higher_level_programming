#!/usr/bin/python3
num1, operator, num2 = input("Enter Calculation: ").split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
	result = num1 + num2
elif operator == "-":
	result = num1 - num2
elif operator == "*":
	result = num1 * num2
elif operator == "/":
	result = num1 / num2
	
print("{} {} {} = {}".format(num1, operator, num2, result))
