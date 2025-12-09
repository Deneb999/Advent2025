from functools import reduce

with open("input.txt", "r") as file:
    input = file.read().split("\n")

input = [[e for e in l.split(" ") if e != ""] for l in input]

total = 0
for i in range(len(input[-1])):
    operands = [int(input[j][i]) for j in range(len(input)-1)]
    if input[-1][i] == "*":
        total+=reduce(lambda x, y: x*y, operands)
    elif input[-1][i] == "+":
        total += reduce(lambda x, y: x + y, operands)

print(total)