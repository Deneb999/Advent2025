with open("input.txt", "r") as file:
    input = file.read().split("\n")


shapes = dict()
sizes = dict()
for idx, line in enumerate(input):
    if line == "":
        shapes[index] = shape
        sizes[index] = area
    elif "x" not in line and ":" in line:
        index = int(line[:-1])
        shape = []
        area = 0
    elif "#" in line or "." in line:
        shape.append(line)
        area+=sum([1 for l in line if l == "#"])
    else:
        break

count = 0
for line in input[idx:]:
    elements = line.split(" ")
    coord = elements[0][:-1].split("x")
    x = int(coord[0])
    y = int(coord[1])
    area = x*y
    tree_shapes = [int(element) for element in elements[1:]]
    total_shape_area = sum([sizes[s]*tree_shapes[s] for s in range(len(tree_shapes))])
    if total_shape_area > area:
        continue #Discard impossible combinations
    count+=1

"""Sooo, this works. I was trying to filter out impossible combinations first to reduce the problem, 
    when I noticed there were actually lots of them (I was expecting none or a few)
    Just to shoot my shot before starting to build an impossible complex solution, I shot my shot with this
    number, and...
    It's correct.
    Apparently, the puzzle is designed so that every tree either has no space enough, or way too much leeway.
    So this is the expected solution.
    I can't say anything else, except that this problem was way too complex (look up packing problems) to build
    an actual solution without any tricks in the input, and that merry Christmas
    """
print(count)