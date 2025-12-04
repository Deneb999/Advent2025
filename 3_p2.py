with open("input.txt", "r") as f:
    input = [line.rstrip("\n") for line in f]


max_vol = 0
for line in input:
    s = str(line)
    l = [int(x) for x in s]

    bank=0
    for i in range(12):
        if i == 11:
            sublist = l
        else:
            sublist = l[0:(-11+i)]
        n = max(sublist)
        l = l[l.index(n)+1:]
        bank*=10
        bank+=n
    max_vol+=bank

print(max_vol)
