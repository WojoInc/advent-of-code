from sys import argv

def filter_rec (mfb, i, inputs) -> list:
    # Break out of the recursion
    if i >= (len(inputs[0])-1):
        return inputs
    if len(inputs) == 1:
        return inputs
    high = []
    low = []
    for line in inputs:
        if int(line[i]) == 1:
            high.append(line)
        else:
            low.append(line)
    if mfb:
        if len(high) > len(low):
            return filter_rec(mfb, i+1, high)
        if len(high) == len(low):
            return filter_rec(mfb, i+1, high)
        return filter_rec(mfb, i+1, low)
    if len(high) > len(low):
            return filter_rec(mfb, i+1, low)
    if len(high) == len(low):
            return filter_rec(mfb, i+1, low)
    return filter_rec(mfb, i+1, high)


with open(argv[1], 'r') as infile:
    input = infile.readlines()
    oxy = filter_rec(True, 0, input)[0]
    co2 = filter_rec(False, 0, input)[0]
    oxy_rating = int(oxy, base=2)
    print(f"Oxygen: {oxy_rating}")
    co2_rating = int(co2, base=2)
    print(f"CO2: {co2_rating}")
    print(f"Life Support: {oxy_rating * co2_rating}")
