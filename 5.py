with open("input.txt", "r") as f:
    input = [line.rstrip("\n") for line in f]

fresh_ingredients = {}
for index, r in enumerate(input):
    if r == "":
        break
    bounds = r.split("-")
    low, high = (int(bounds[0]), int(bounds[1]) + 1)
    sizes = range(len(bounds[0]), len(bounds[1])+1)
    for s in sizes:
        if s not in fresh_ingredients:
            fresh_ingredients[s] = list()
        fresh_ingredients[s].append((low, high))


n_fresh = 0
for ingredient in input[index+1:]:
    i = len(str(ingredient))
    try:
        for low,high in fresh_ingredients[i]:
            if int(ingredient)>=low and int(ingredient)<=high:
                n_fresh+=1
                break
    except KeyError:
        continue
print(n_fresh)
