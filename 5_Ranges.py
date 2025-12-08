from Ranges import Range

with open("input.txt", "r") as f:
    input = [line.rstrip("\n") for line in f]

part_two = True

rs = Range(1,-1)#Empty
for index, r in enumerate(input):
    if r == "":
        break
    bounds = r.split("-")
    low, high = (int(bounds[0]), int(bounds[1]))
    r = Range(low, high)
    l = len(r)
    rs = rs.union(r)

if part_two:
    n_fresh = sum(len(r) for r in rs.ranges)
else:
    n_fresh = 0
    for ingredient in input[index+1:]:
        if int(ingredient) in rs:
            n_fresh+=1

print(n_fresh)