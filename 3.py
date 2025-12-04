with open("input.txt", "r") as f:
    input = [line.rstrip("\n") for line in f]

max_vol = 0
for line in input:
    s = str(line)
    l = [int(x) for x in s]
    first = max(l[0:-1])
    rest_of_list = l[l.index(first)+1:]
    second = max(rest_of_list)
    max_vol+=10*first+second

print(max_vol)
