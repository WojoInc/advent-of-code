from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readlines()
    sum = 0
    for line in input:
        segments = {}
        patterns, output = line.split(' | ')
        patterns = patterns.split(' ')
        output = output.strip('\n').split(' ')
        segments[1] = set()
        pat235 = []
        pat069 = []
        segments[4] = set()
        segments[7] = set()
        segments[8] = set(['a','b','c','d','e','f', 'g'])
        for p in patterns:
            if len(p) == 2:
                segments[1] = set(p)
            if len(p) == 3:
                segments[7] = set(p)
            if len(p) == 4:
                segments[4] = set(p)
            if len(p) == 5:
                pat235.append(set(p))
            if len(p) == 6:
                pat069.append(set(p))
        # Find 0,6,9
        for s in pat069:
            # of 0,6,9, 6 is the only one in which only 1 segment of 1 can appear
            if len(segments[1] - s) == 1:
                segments[6] = s
            if len(segments[4] - s) == 1:
                if len(segments[7] - s) == 0:
                    segments[0] = s
        pat069.remove(segments[0])
        pat069.remove(segments[6])
        segments[9] = pat069[0]
        # Find 2,3,5
        for s in pat235:
            # of 2,3,5, 3 is the one where set difference of 3 - 1 = 3
            if len(s - segments[1]) == 3:
                segments[3] = s
            if len(segments[6] - s) == 1:
                segments[5] = s
        pat235.remove(segments[3])
        pat235.remove(segments[5])
        segments[2] = pat235[0]

        outstring = ""
        for s in output:
            for i in range(10):
                if set(s) == segments[i]:
                    outstring += str(i)
                    break
        sum += int(outstring)
            
    print(sum)

