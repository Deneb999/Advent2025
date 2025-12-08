from itertools import product
from math import sqrt, prod
from tqdm import tqdm

with open("input.txt", "r") as file:
    input = file.read().split("\n")

def distance(a,b):
    a = [int(x) for x in a.split(",")]
    b = [int(x) for x in b.split(",")]
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def n_connections(sets):
    return sum([len(s)-1 for s in sets])


connections = []
for idx, a in tqdm(enumerate(input)):
    for b in input[idx+1:]:
        d = distance(a,b)
        if d!= 0:
            connections.append((d,a,b))

connections.sort(key=lambda c: c[0])
connections = connections
connections = [(c[1], c[2]) for c in connections]

circuits = []
for connection in connections:
    already_connected = None
    to_connect = None
    to_remove = []
    for idx, c in enumerate(circuits):
        pre_c = c
        if connection[0] in c or connection[1] in c:
            c.add(connection[0])
            c.add(connection[1])
            if already_connected is not None:
                circuits[already_connected] = circuits[already_connected].union(c)
                to_remove.insert(0, idx)
            else:
                already_connected = idx
    for idx in to_remove:
        c2 = circuits.pop(idx)
    if len(circuits) == 1 and len(circuits[0]) == len(input):
        print(int(connection[0].split(",")[0]) * int(connection[1].split(",")[0]))
        exit()
    if already_connected is None:
            circuits.append({connection[0], connection[1]})

circuits.sort(key=lambda c: len(c), reverse=True)
print(prod(len(c) for c in circuits[0:3]))