with open("input.txt", "r") as file:
    input = file.read().split("\n")

#Note: today I started the advent just as it opened. Second star gotten after 25 mins
beams = {input[0].index("S"):1}
split = 0
for input in input[1:]:
    new_beams = dict()
    for beam in beams:
        value = beams[beam]
        if input[beam] == "^":
            if beam-1 not in new_beams:
                new_beams[beam-1] = 0
            if beam+1 not in new_beams:
                new_beams[beam+1] = 0
            new_beams[beam-1] += value
            new_beams[beam+1] += value
            split +=1
        else:
            if beam not in new_beams:
                new_beams[beam] = 0
            new_beams[beam] += value

    beams = new_beams
print(sum(beams.values()))