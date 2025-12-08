with open("input.txt", "r") as f:
    input = [line.rstrip("\n") for line in f]

ranges = {}
for index, r in enumerate(input):
    if r == "":
        break
    bounds = r.split("-")
    low, high = (int(bounds[0]), int(bounds[1]))
    sizes = range(len(bounds[0]), len(bounds[1])+1)
    for s in sizes:
        trimmed_low = max(low,10**(s-1))
        trimmed_high = min(high,(10**s)-1)
        if s not in ranges:
            ranges[s] = []
        found_range = None
        second_range = None

        scrap = []
        for i, r in enumerate(ranges[s]):
            if r["low"]>= trimmed_low and r["high"]<=trimmed_high:
                scrap.append(i)
        for i in reversed(scrap):
            ranges[s].pop(i)

        for i, r in enumerate(ranges[s]):
            if r["low"]<=trimmed_low<=r["high"] or r["low"]<=trimmed_high<=r["high"]:
                r["low"] = min(r["low"], trimmed_low)
                r["high"] = max(r["high"], trimmed_high)
                if found_range is None:
                    found_range = i
                else:
                    second_range = i
                    break
        if second_range: #combine ranges
            second_range = ranges[s].pop(second_range)
            first_range = ranges[s].pop(found_range)
            ranges[s].append({"low": min(first_range["low"],second_range["low"]),
                              "high": max(first_range["high"],second_range["high"])})
        if found_range is None:
            ranges[s].append({"low":trimmed_low, "high":trimmed_high})
        ranges[s].sort(key=lambda d: d["low"]) #sanity
fresh = 0
for s in ranges.values():
    for r in s:
        fresh+=r["high"]-r["low"]+1
print(fresh)