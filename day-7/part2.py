from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readline().split(',')
    # Could dynamically figure out the size needed for the array, too lazy though
    # So we're using 2000, which is larger than the largest input value I got
    buckets = [0] * 2000
    for s in input:
        for i in range(len(buckets)):
            buckets[i] += sum(range(abs(int(s) - int(i))+1))
    lowest = buckets[0]
    pos = 0
    for i in range(len(buckets)):
        if buckets[i] < lowest:
            lowest = buckets[i]
            pos = i
    fuel = 0
    # print(buckets)
    for s in input:
        fuel += sum(range(abs(int(s)-pos)+1))
    print(pos)
    print(fuel)