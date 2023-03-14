#!/usr/bin/python3
tall = input("How tall is the tree: ")
tall = int(tall)
i = 1
hashes = 1

while i <= tall:
    for j in range(tall - i):
        print(end=" ")
    for k in range(hashes):
        print("#", end="")
    hashes += 2
    print("")
    i += 1
for l in range(tall - 1):
    print(end=" ")
print("#")
