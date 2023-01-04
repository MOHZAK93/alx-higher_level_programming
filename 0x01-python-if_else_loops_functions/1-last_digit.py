#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
text = "Last digit of"
mod = abs(number) % 10
if number < 0:
    mod = mod * -1
print(mod)
if mod > 5 and number > 0:
    print("{} {} is {} and is greater than 5".format(text, number, mod))
elif mod == 0:
    print("{} {} is {} and is 0".format(text, number, mod))
elif mod < 6:
    print("{} {} is {} and is less than 6 and not 0".format(text, number, mod))
