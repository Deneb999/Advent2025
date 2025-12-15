from functools import lru_cache
from math import inf
from unittest.mock import sentinel

from tqdm import tqdm

with open("input.txt", "r") as file:
    input = file.read().split("\n")

@lru_cache(maxsize=None)
def press(machine, button):
    button = [int(b) for b in button.replace("(","").replace(")","").split(",")]
    for light in button:
        if machine[light] == ".":
            machine = machine[:light] + "#" + machine[light+1:]
        else:
            machine = machine[:light] + "." + machine[light+1:]
    return machine


seen_states = {0:set()}
def count_number_of_presses(machine, buttons, machine_final, carry=0):
    global seen_states
    if carry == 0:
        seen_states = {0: set()}
    if machine == machine_final:
        return carry

    if carry not in seen_states:
        seen_states[carry] = seen_states[carry-1]

    states = []
    my_seen_states = set()
    for button in buttons:
        s = (press(machine, button))
        if s not in seen_states[carry]:
            states.append(s)
        my_seen_states.add(s)
    if len(states) == 0:
        return inf
    seen_states[carry] = seen_states[carry].union(my_seen_states)
    return min([count_number_of_presses(state, buttons, machine_final, carry=(carry+1)) for state in states])

sum = 0
for line in tqdm(input):
    line = line.split(" ")
    machine_final = line[0][1:-1]
    buttons = line[1:-1]
    state = machine_final.replace("#",".")
    sum += count_number_of_presses(state, buttons, machine_final)

print(sum)