with open("input.txt", "r") as f:
        input = [line.rstrip("\n") for line in f]

part_two=True

zeroes = 0
pos = 50

for element in input:
    moves = int(element[1:])
    if element[0] == "L":
        moves*=-1
    prev_pos = pos
    pos+=moves

    if not part_two:
        pos=pos%100
        if pos == 0:
            zeroes+=1
    else:
        while pos>100:
            pos-=100
            zeroes+=1
        while pos<0:
            pos+=100
            if prev_pos!=0:
                zeroes+=1
            else:
                prev_pos=pos%100
        if pos%100==0:
            zeroes+=1
            pos = 0
print(zeroes)