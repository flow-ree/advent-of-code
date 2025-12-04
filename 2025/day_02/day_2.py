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

        # only even product ids
        if (productIdLength % 2 == 0):

            # get parts
            part_1 = str(productId)[0:int(productIdLength/2)]
            part_2 = str(productId)[int(productIdLength/2):]
            if (part_1 == part_2):
                invalidProductIds.append(productId)
                sum += productId


print("The result is: " + str(sum))