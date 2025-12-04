#!/usr/bin/env python3

filename ="input.txt"
pointing = 50
result = 0
passes = 0
with open(filename) as file:
    while line := file.readline():
        direction = line.rstrip()[0]
        steps = int(line.rstrip()[1:])
        p = 0
        previous = pointing
        # rotate right direction
        if (direction == "L"): pointing -= steps
        elif (direction == "R"): pointing += steps
        total = pointing
        # see how many times passes 0
        

        # when outside of wheel range, align with modulo
        if(pointing < 0 or pointing >= 100):            
            pointing = pointing % 100
            
            p += abs(total) // 100
            if total < 0 and previous != 0:
                p += 1
        if total == 0: p += 1
        # add to result when pointing 0
        #if(pointing == 0): 
        #    result += 1
        passes += p
        print(str(previous) + "\t" + line.rstrip() + "\t" + str(total) + " \t" + str(pointing) + "\t" + str(p))

print("The result is: " + str(result))
print("The passes is: " + str(passes))
print("The result with passes is: " + str(result + passes))

# Correct: 5815