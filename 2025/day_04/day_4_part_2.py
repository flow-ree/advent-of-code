#!/usr/bin/env python3
import os

script_dir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(script_dir, filename)

maxSurroundingRolls = 3
currentGrid = []
sum = 0
canRemoveRolls = True

# store values in grid
file = open(filepath)
for line in file:
    currentGrid.append(list(line.rstrip()))
    
def removeRolls (grid):
    global currentGrid
    removedRolls = 0

    # iterate grid
    for lineIndex, line in enumerate(grid):
        for positionIndex, item in enumerate(line):

            # when roll found, check if can be removed
            if item == '@':
                surrounded = []
                startSurroundedLineIndex = lineIndex - 1 if lineIndex > 0 else 0
                endSurroundedLineIndex = lineIndex + 1 if lineIndex+1 < len(grid) else lineIndex
                startSurroundedPositionIndex = positionIndex - 1 if positionIndex > 0 else 0
                endSurroundedPositionIndex = positionIndex + 1 if positionIndex + 1 < len(line) else positionIndex

                # check sourrounded items
                for y in range(startSurroundedLineIndex, endSurroundedLineIndex + 1):
                    for x in range(startSurroundedPositionIndex, endSurroundedPositionIndex + 1):
                        if y != lineIndex or x != positionIndex:
                            if grid[y][x] == "@":
                                surrounded.append(grid[y][x])

                # remove roll when possible
                if len(surrounded) <= maxSurroundingRolls:
                    removedRolls += 1
                    currentGrid[lineIndex][positionIndex] = "X"
    
    return removedRolls

while canRemoveRolls:
    removedRolls = removeRolls(currentGrid)
    sum += removedRolls
    if removedRolls < 1:
        canRemoveRolls = False
        
print("The result is: " + str(sum))