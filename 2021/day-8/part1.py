from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readlines()
    sum = 0
    for line in input:
        segments, output = line.split(' | ')
        segments = segments.split(' ')
        output = output.strip('\n').split(' ')
        for s in output:
            if len(s) in [2,3,4,7]:
                sum +=1
    print(sum)

