with open("input.txt", "r") as file:
    input = file.read().split("\n")

#Note: today I started the advent just as it opened. First star gotten in 5 minutes
beams = {input[0].index("S")}
split = 0
for input in input[1:]:
    new_beams = set()
    for beam in beams:
        if input[beam] == "^":
            new_beams.add(beam-1)
            new_beams.add(beam +1)
            split +=1
        else:
            new_beams.add(beam)
    beams = new_beams
print(split)