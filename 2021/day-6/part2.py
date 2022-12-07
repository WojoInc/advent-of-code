from sys import argv

with open(argv[1], 'r') as infile:
    fish = {
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
        "1": 0,
        "0": 0
    }
    for i in infile.readline().strip("\n").split(","):
        fish[i] += 1
    print(fish)        
    for i in range(256):
        for i in range(0,10):
            if i == 0:
                fish["7"] += fish["0"]
                fish["9"] += fish["0"]
                fish["0"] = 0
                continue
            fish[str(i-1)] += fish[str(i)]
            fish[str(i)] = 0
    sum = 0
    for i in range(0,10):
        sum += fish[str(i)]
    print(f"Number of fish {sum}")
