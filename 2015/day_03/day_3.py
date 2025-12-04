#!/usr/bin/env python3
import os

script_dir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(script_dir, filename)

positionX = 0
positionY = 0
positionSantaX = 0
positionSantaY = 0
positionRobotX = 0
positionRobotY = 0
housesVisited = ["0-0"]
housesVisitedP2 = ["0-0", "0-0"]

file = open(filepath)
line = file.readline()
for index, character in enumerate(line):
    match character:
        case "<":
            positionX -=1
            if index % 2 == 0:
                positionSantaX -= 1
            else:
                positionRobotX -= 1
        case ">":
            positionX +=1
            if index % 2 == 0:
                positionSantaX += 1
            else:
                positionRobotX += 1
        case "^":
            positionY +=1
            if index % 2 == 0:
                positionSantaY += 1
            else:
                positionRobotY += 1
        case "v":
            positionY -=1
            if index % 2 == 0:
                positionSantaY -= 1
            else:
                positionRobotY -= 1
    housesVisited.append(str(positionX) + "-" + str(positionY))
    housesVisitedP2.append(str(positionSantaX) + "-" + str(positionSantaY))
    housesVisitedP2.append(str(positionRobotX) + "-" + str(positionRobotY))
print(housesVisited)
totalHousesVisited = set(housesVisited)
totalHousesVisitedP2 = set(housesVisitedP2)

print("The total number of houses visited is: " + str(len(totalHousesVisited)))
print("[P2] The total number of houses visited is: " + str(len(totalHousesVisitedP2)))
