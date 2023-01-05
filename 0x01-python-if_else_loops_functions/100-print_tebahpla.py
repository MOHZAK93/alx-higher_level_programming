#!/usr/bin/python3
i = 26
while i:
    if (i % 2 == 0):
        j = i + 96
    else:
        j = i + 64
    print("{}".format(chr(j)), end="")
    i -= 1
