from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readlines()
    count = 0
    ocean = {}
    for line in input:
        points = line.strip("\n").split(" -> ")
        p1 = points[0].split(',')
        p2 = points[1].split(',')
        if int(p1[0]) == int(p2[0]):
            if int(p1[1]) > int(p2[1]):
                a =  int(p2[1])
                b = int(p1[1]) +1
            else:
                b =  int(p2[1]) +1
                a = int(p1[1])
            for i in range(a,b):
                point = p1[0] + "," + str(i)
                if point not in ocean:
                    ocean[point] = 1
                else:
                    ocean[point] += 1
                if ocean[point] == 2:
                    count +=1
        elif int(p1[1]) == int(p2[1]):
            if int(p1[0]) > int(p2[0]):
                a =  int(p2[0])
                b = int(p1[0])+1
            else:
                b =  int(p2[0])+1
                a = int(p1[0])
            for i in range(a,b):
                point = str(i) + "," + p1[1]
                if point not in ocean:
                    ocean[point] = 1
                else:
                    ocean[point] += 1
                if ocean[point] == 2:
                    count +=1
    print(count)
