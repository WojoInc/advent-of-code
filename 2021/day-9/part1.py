from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readlines()
    delta = len(input[0])
    inputstring = []
    for row in input:
        inputstring.extend(row)
    sum = 0
    for i in range(len(inputstring)):
        v = inputstring[i]
        low = True
        if inputstring[i-1] > v:
            low = False
        if inputstring[]