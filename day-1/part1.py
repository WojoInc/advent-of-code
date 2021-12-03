from sys import argv

with open(argv[1], 'r') as infile:
    count = 0
    input = infile.readlines()
    last = int(input[0])
    for cursor in input:
        if int(cursor) > last: 
            count+=1
        last=int(cursor)
    print(count)
    