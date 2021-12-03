from sys import argv

with open(argv[1], 'r') as infile:
    count = 0
    input = infile.readlines()
    for i in range(0, len(input)-3, 1):
        win1 = int(input[i]) + int(input[i+1]) + int(input[i+2])
        win2 = int(input[i+1]) + int(input[i+2]) + int(input[i+3])
    print(count)
    