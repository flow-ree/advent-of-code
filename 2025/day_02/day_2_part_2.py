#!/usr/bin/env python3

filename ="input.txt"
invalidProductIds = []
sum = 0

file = open(filename)
line = file.readline()
productRanges = line.rstrip().split(',')
for productRange in productRanges:

    # get start and end of range
    start = int(productRange.split('-')[0])
    end = int(productRange.split('-')[1])

    print("Product range: " + str(start) + " - " + str(end))

    # iterate product ids
    for productId in range(start, end+1):

        productIdLength = len(str(productId))
        divisors = []

        #print("Product-ID: " + str(productId))
        # find divisors
        for d in range(1,productIdLength//2 + 1):
            if (productIdLength % d) == 0: 
                divisors.append(d)
        
        #print(divisors)
        found = False
        for divisor in divisors:
            substrings = []
            for index in range(1,(productIdLength // divisor) + 1):
                substrings.append(str(productId)[(divisor * index - divisor):(divisor * index)])
            #print(substrings)
            if all(substring == substrings[0] for substring in substrings):
                found = True
        if found:
            print(productId)
            invalidProductIds.append(productId)
            sum += productId


        #print("===")

print("The result is: " + str(sum))
# 48631958998