from functools import total_ordering

with open("input.txt", "r") as f:
    input = f.read().split("\n")

part_2 = True

map = {}
y = 0
for line in input:
    x= 0
    for element in line:
        map[(x,y)] = {"paper":element=="@", "neighbours":0}
        x+=1
    y+=1

for x,y in map:
    if map[(x,y)]["paper"]:
        for coor in [(x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]:
            try:
                if map[coor]["paper"]:
                    map[(x,y)]["neighbours"]+=1
                    map[coor]["neighbours"]+=1
            except KeyError:
                pass



def compute():
    global map
    count = 0
    for x,y in map:
        e = map[(x,y)]
        if e["paper"] and e["neighbours"]<4:
            count+=1
            if part_2:
                e["paper"] = False
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        try:
                            if map[(x+i,y+j)]["paper"]:
                                map[(x+i, y+j)]["neighbours"]-=1
                        except KeyError:
                            pass
    return count

if part_2:
    total_count = 0
    while True:
        c = compute()
        total_count+=c
        if c == 0:
            break
else:
    total_count = compute()

print(total_count)