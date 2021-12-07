from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readline().split(',')
    buckets = [0] * 2000
    for s in input:
        for i in range(len(buckets)):
            buckets[i] += abs(int(s) - i)
    lowest = buckets[0]
    pos = 0
    for i in range(len(buckets)):
        if buckets[i] < lowest:
            lowest = buckets[i]
            pos = i
    fuel = 0
    # print(buckets)
    for s in input:
        fuel += (abs(int(s)-pos))
    print(pos)
    print(fuel)