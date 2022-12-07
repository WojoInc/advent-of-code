from sys import argv



with open(argv[1], 'r') as infile:
    input = [i for i in map(int,infile.readline().strip("\n").split(","))]
    numfish = len(input)
    for i in range(80):
        for j in range(numfish):
            if input[j] == 0:
                input.append(8)
                input[j] = 6
                continue
            input[j] -= 1
        numfish = len(input)
    print(f"Number of fish {len(input)}")
    