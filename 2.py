with open("input.txt", "r") as file:
    content = file.read().strip().split(",")

count = 0
invalid_ids = {}
for e in content:
    bounds = e.split("-")
    for r in range(int(bounds[0]),int(bounds[1])+1):
        s = str(r)
        length = len(s)
        if length%2!=0:
            continue
        divisor = 10 ** (length/2) + 1
        if r % divisor == 0:
            invalid_ids[s] = length
            count += r
print(count)
print(invalid_ids)