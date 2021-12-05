from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readlines()
    count = 0
    ocean = {}
    for line in input:
        points = line.strip("\n").split(" -> ")
        p1 = points[0].split(',')
        p2 = points[1].split(',')
        x, y = 0, 0

        if int(p1[0]) > int(p2[0]):
            x = -1
        elif int(p1[0]) < int(p2[0]):
            x = 1
        if int(p1[1]) > int(p2[1]):
            y = -1
        elif int(p1[1]) < int(p2[1]):
            y = 1
        
        nextx = int(p1[0])
        nexty = int(p1[1])
        while (nextx != int(p2[0])) or (nexty != int(p2[1])):
            nextp = str(nextx) +","+ str(nexty)
            if nextp not in ocean:
                ocean[nextp] = 1
            else:
                ocean[nextp] += 1
            if ocean[nextp] == 2:
                count +=1
            nextx += x
            nexty += y
        nextp = str(nextx) +","+ str(nexty)
        if nextp not in ocean:
            ocean[nextp] = 1
        else:
            ocean[nextp] += 1
        if ocean[nextp] == 2:
            count +=1
    print(count)
