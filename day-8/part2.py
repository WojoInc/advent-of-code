from sys import argv

decode = {18:0,7:1,15:2,16:3,11:4,15:5,19:6,7:7,21:8,17:9}

with open(argv[1], 'r') as infile:
    input = infile.readlines()
    for line in input:
        segments = {}
        patterns, output = line.split(' | ')
        patterns = patterns.split(' ')
        output = output.strip('\n').split(' ')
        pat1 = ""
        pat235 = {}
        pat4 = ""
        pat7 = ""
        for p in patterns:
            if len(p) == 2:
                pat1 = p
            if len(p) == 3:
                pat7 = p
            if len(p) == 4:
                pat4 = p
            if len(p) == 5:
                for c in p:
                    if c not in pat235:
                        pat235[c] = 1
                    else:
                        pat235[c] += 1
            if "" not in [pat1,pat4,pat7]:
                break
        segments[pat7.replace(pat1[0],'').replace(pat1[1],'')] = 0
        segments[pat1[0]] = {2,5}
        segments[pat1[1]] = {2,5}
        segments[pat4.replace(pat1[0],'').replace(pat1[1],'')[0]] = {1,3}
        segments[pat4.replace(pat1[0],'').replace(pat1[1],'')[1]] = {1,3}
        max = 0
        maxk = ""
        for k,v in pat235.items():
            if v > max:
                max = v
                maxk = k
        segments[maxk] = 3
        print("")
            
    print(sum)

