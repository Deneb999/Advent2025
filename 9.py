with open("input.txt", "r") as file:
    input = file.read().split("\n")

def distance(a,b):
    a = [int(x) for x in a.split(",")]
    b = [int(x) for x in b.split(",")]
    return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)


max_distance = 0
for idx, a in enumerate(input):
    for b in input[idx+1:]:
        d = distance(a,b)
        if d>max_distance:
            max_distance = d

print(max_distance)