from ortools.linear_solver import pywraplp
from sys import stdout
from unittest.mock import sentinel
from tqdm import tqdm

"""
Solved via linear programming. The following tutorial was very helpful
https://mlabonne.github.io/blog/posts/2022-03-02-Linear_Programming.html
"""

with open("input.txt", "r") as file:
    input = file.read().split("\n")

def str_to_list(s):
    return [int(i) for i in s[1:-1].split(",")]

s=0
for line in tqdm(input):
    line = line.split(" ")
    machine_final = str_to_list(line[-1])
    buttons = [str_to_list(b) for b in line[1:-1]]
    solver = pywraplp.Solver('Solver', pywraplp.Solver.SAT_INTEGER_PROGRAMMING)
    button_vars = dict()
    for i, b in enumerate(buttons):
        button_vars[i] = solver.IntVar(0, solver.infinity(), f"Button {i}")
    for idx,m in enumerate(machine_final):
        used_buttons = []
        for j, b in enumerate(buttons):
            if idx in b:
                used_buttons.append(j)
        used_vars = [button_vars[b] for b in used_buttons]
        v = sum(used_vars)
        solver.Add(v == m)
    solver.Minimize(sum([button_vars[b] for b in button_vars]))
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        value = solver.Objective().Value()
        value2 = int(value)
        s+=value2
        for b in button_vars:
            value3 = button_vars[b].solution_value()
        pass
    else:
        print("Error")
print(s)