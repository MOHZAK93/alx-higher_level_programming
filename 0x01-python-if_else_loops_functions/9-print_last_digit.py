#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    result = number % 10
    print(result, end="")
    return (result)
