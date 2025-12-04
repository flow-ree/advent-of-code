#!/usr/bin/env python3
import os

script_dir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(script_dir, filename)

total = 0
totalRibbon = 0
file = open(filepath)
for line in file:
    dimensions = list(map(int, line.rstrip().split('x')))
    dimensions.sort()
    firstArea = dimensions[0] * dimensions[1]
    secondArea = dimensions[0] * dimensions[2]
    thirdArea = dimensions[1] * dimensions[2]
    total += 3*firstArea + 2*secondArea + 2* thirdArea
    totalRibbon += dimensions[0] * dimensions[1] *dimensions[2] + 2*dimensions[0] + 2*dimensions[1]
        
print("The total square feet of wrapping paper is: " + str(total))
print("The total feet of ribbon is: " + str(totalRibbon))