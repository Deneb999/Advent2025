from functools import lru_cache

from tqdm import tqdm

from Ranges import Range, RangeSet

with open("input.txt", "r") as file:
    input = file.read().split("\n")

def distance(a,b):
    a = [int(x) for x in a.split(",")]
    b = [int(x) for x in b.split(",")]
    return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)

"""Note: this function only checks that the rectangle is either completely inside or completely outside
the shape. For this particular problem it's (in practical terms) equivalent, but if we wanted to be more
formal, we could pathfind any point of the rectangle to a point that we know is in the outside (or inside)
of the shape, and see whether we cross any green tile. 
Alternatively, we could store a direction along the green tiles, pointing always to either the outside
or to the inside. This is topologically consistent.
"""
def is_valid(a,b):
    _a = [int(x) for x in a.split(",")]
    _b = [int(x) for x in b.split(",")]
    a_x = _a[0]
    a_y = _a[1]
    b_x = _b[0]
    b_y = _b[1]
    for x in range(min(a_x, b_x)+1, max(a_x, b_x)):
        if (x,min(a_y, b_y)+1) in green_tiles or (x,max(a_y, b_y)-1) in green_tiles:
            return False
    for y in range(min(a_y, b_y)+1, max(a_y, b_y)):
        if (min(a_x, b_x)+1,y) in green_tiles or (max(a_x, b_x)-1,y) in green_tiles:
            return False
    return True

green_tiles = set()
def add_greens(a,b):
    global green_tiles
    a_x, a_y = a.split(",")
    b_x, b_y = b.split(",")
    a_x, a_y = int(a_x), int(a_y)
    b_x, b_y = int(b_x), int(b_y)
    if b_x < a_x:
        x_range = (b_x, a_x)
    elif b_x > a_x:
        x_range = (a_x, b_x)
    else:
        x_range = (a_x, a_x)

    if b_y < a_y:
        y_range = (b_y, a_y)
    elif b_y > a_y:
        y_range = (a_y, b_y)
    else:
        y_range = (a_y, a_y)

    for i in range(x_range[0], x_range[1]+1):
        for j in range(y_range[0], y_range[1]+1):
            green_tiles.add((i,j))

for idx, a in enumerate(input):
    try:
        b = input[idx+1]
    except IndexError:
        b = input[0]
    add_greens(a,b)


max_distance = 0
for idx, a in tqdm(enumerate(input)):
    for b in input[idx+1:]:
        d = distance(a,b)
        if d > max_distance:
            if is_valid(a,b):
                max_distance = d
                print(max_distance)


print("------")
print(max_distance)