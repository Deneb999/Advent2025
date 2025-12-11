from functools import lru_cache

with open("input.txt", "r") as file:
    input = file.read().split("\n")


@lru_cache(maxsize=None)
def all_paths_from(node, destination="out", exclude=None):
    if node == destination:
        return [[destination]]
    final_paths = []
    for neighbour in neighbours[node]:
        if exclude == neighbour:
            continue
        for path in all_paths_from(neighbour, destination, exclude):
            final_paths.append([node] + path)
    return final_paths

@lru_cache(maxsize=None)
def count_paths_from(node, destination="out", exclude=None):
    if node == destination:
        return 1
    possible_paths = 0
    for neighbour in neighbours[node]:
        if exclude == neighbour:
            continue
        c = count_paths_from(neighbour, destination, exclude)
        possible_paths+=c
    return possible_paths


finished_paths = set()
neighbours = {"out":set()}
neighbours_reversed = {}
for line in input:
    line = line.split()
    origin = line[0][:-1]
    destinations = line[1:]
    neighbours[origin] = set(destinations)
    for d in destinations:
        if d not in neighbours_reversed:
            neighbours_reversed[d] = set()
        neighbours_reversed[d].add(origin)

def part1():
    print(len(all_paths_from("you")))

def part2():
    srv_dac = count_paths_from("svr",destination="dac", exclude="fft")
    print("Svr-Dac",srv_dac)
    srv_fft = count_paths_from("svr", destination="fft", exclude="dac")
    print("Svr-Fft",srv_fft)
    dac_fft = count_paths_from("dac", destination="fft")
    print("Dac-Fft",dac_fft)
    fft_dac = count_paths_from("fft", destination="dac")
    print("Ftt-Dac",fft_dac)
    dac_out = count_paths_from("dac", destination="out", exclude="fft")
    print("Dac-Out",dac_out)
    fft_out = count_paths_from("fft", destination="out", exclude="dac")
    print("Ftt-Out",fft_out)
    print(f"Solution:  {srv_dac*dac_fft*fft_out + srv_fft*fft_dac*dac_out}")

part2()