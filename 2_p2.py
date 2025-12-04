from math import sqrt, ceil

with open("input.txt", "r") as file:
    content = file.read().strip().split(",")

length_divisors = {}
def get_length_divisors(length):
    global length_divisors
    if length in length_divisors:
        return length_divisors[length]
    l_d = set()
    for i in range(1, ceil(sqrt(length)) + 1):
        if length % i == 0:
            l_d.add(int(i))
            l_d.add(int(length / i))
    #l_d.remove(1)
    length_divisors[length] = l_d
    return l_d

def get_invalid_checkers(length):
    invalids = []
    for d in get_length_divisors(length):
        other_divisor = int(length / d)
        total_divisor = 1
        for i in range(d - 1):
            total_divisor *= 10 ** (other_divisor)
            total_divisor += 1
        if total_divisor!=1:
            invalids.append(total_divisor)
    return invalids

count = 0
invalid_ids = {}
for e in content:
    bounds = e.split("-")
    for r in range(int(bounds[0]),int(bounds[1])+1):
        s = str(r)
        length = len(s)
        for i in get_invalid_checkers(length):
            if r%i==0:
                count+=r
                invalid_ids[r] = i
                break



print(count)
print(invalid_ids)
