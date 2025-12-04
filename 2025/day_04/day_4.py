#!/usr/bin/env python3
import os

script_dir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(script_dir, filename)

maxSurroundingRolls = 3
grid = []
sum = 0

# store values in grid
file = open(filepath)
for line in file:
    grid.append(list(line.rstrip()))
    
# iterate grid
for lineIndex, line in enumerate(grid):
    for positionIndex, item in enumerate(line):

        # when roll found, check surrounded items
        if item == '@':
            surrounded = []
            startSurroundedLineIndex = lineIndex - 1 if lineIndex > 0 else 0
            endSurroundedLineIndex = lineIndex + 1 if lineIndex+1 < len(grid) else lineIndex
            startSurroundedPositionIndex = positionIndex - 1 if positionIndex > 0 else 0
            endSurroundedPositionIndex = positionIndex + 1 if positionIndex + 1 < len(line) else positionIndex

            for y in range(startSurroundedLineIndex, endSurroundedLineIndex + 1):
                for x in range(startSurroundedPositionIndex, endSurroundedPositionIndex + 1):
                    if y != lineIndex or x != positionIndex:
                        if grid[y][x] == "@":
                            surrounded.append(grid[y][x])
            if len(surrounded)  <= maxSurroundingRolls:
                sum += 1




print("The result is: " + str(sum))