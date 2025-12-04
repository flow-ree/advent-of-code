#!/usr/bin/env python3

filename ="input.txt"
voltages = []
sum = 0

file = open(filename)
for line in file:
    batteryBank = line.rstrip()
    slot1 = {
        "value": 0,
        "position": 0,
    }
    slot2 = {
        "value": 0,
        "position": 0,
    }
    batteryJoltage = 0
    for idx, slotJoltage in enumerate(batteryBank):
        joltage = int(slotJoltage)
        if (joltage > slot1["value"] and (idx+1) < len(batteryBank)):
            slot1 = {
                "value": joltage,
                "position": idx,
            }
            slot2 = {
                "value": 0,
                "position": 0,
            }
        elif (joltage > slot2["value"]):
            slot2 = {
                "value": joltage,
                "position": idx,
            }

    if (slot1["position"] <= slot2["position"]): 
        batteryJoltage = int(str(slot1["value"]) + str(slot2["value"]))
    else: 
        batteryJoltage = int(str(slot2["value"]) + str(slot1["value"]))


    voltages.append(batteryJoltage)
    print(batteryJoltage)
    sum += batteryJoltage

print("The result is: " + str(sum))