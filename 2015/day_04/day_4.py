#!/usr/bin/env python3
import os
import hashlib

script_dir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(script_dir, filename)

key = "yzbqklnj"
found = False
number = 0
while not found:
    string = key + str(number)
    hash=hashlib.md5(string.encode()).hexdigest()
    print(hash)
    if hash.startswith("000000"):
        found = True
        break
    number += 1

print("The lowest number is: " + str(number))