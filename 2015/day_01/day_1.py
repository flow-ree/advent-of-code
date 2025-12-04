#!/usr/bin/env python3
import os

script_dir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(script_dir, filename)

total = 0

file = open(filepath)
line = file.readline()
for index, character in enumerate(line):
    if character == "(":
        floor += 1
    if character == ")":
        floor -= 1
    if firstBasementPosition == 0 and floor == -1:
        firstBasementPosition = index + 1
    print(character)
        
print("The floor is: " + str(floor))

print("First position entering basement: " + str(firstBasementPosition))