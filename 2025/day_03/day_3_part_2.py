#!/usr/bin/env python3

filename ="input.txt"
totalNumberOfSlots = 12
voltages = []
sum = 0

file = open(filename)
for line in file:
    batteryBank = list(map(int, line.rstrip()))
    slots = []

    for i in range(0, totalNumberOfSlots):
        # create subList to scan remaining slots
        startScanIndex = slots[len(slots) - 1]["index"] + 1 if len(slots) else 0
        endScanIndex = len(batteryBank) - totalNumberOfSlots + i + 1
        subList = batteryBank[startScanIndex:endScanIndex]

        # get max of subList
        index_max = max(range(len(subList)), key=subList.__getitem__)
        slot = {
            "value": subList[index_max],
            "index": startScanIndex + index_max
        }
        slots.append(slot)
    
    joltage = ''.join(map(lambda item: str(item["value"]), slots))
    print(joltage)
    sum += int(joltage)

print("The result is: " + str(sum))

# 168798209663590