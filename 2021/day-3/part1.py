from sys import argv

with open(argv[1], 'r') as infile:
    input = infile.readlines()
    nLines = len(input)
    sums = [0] * (len(input[0])-1) # Set bit width, ignoring newline character
    for line in input:
        for i in range(0, len(line)-1, 1):
            sums[i] += int(line[i])
    # Fori loop here as iterable is readonly, so foreach doesn't work
    for i in range(0, len(sums), 1):
        if sums[i] < (nLines / 2):
            sums[i] = 0
            continue
        sums[i] = 1
    print(f"MFB: {sums}")
    gamma = int("".join(map(str,sums)), base=2)
    print(f"Gamma: {gamma}")
    epsilon = int("".join(map(str,map(lambda x: x^ 1, sums))), base=2)
    print(f"Epsilon: {epsilon}")
    print(f"Power Consumption: {gamma * epsilon}")
