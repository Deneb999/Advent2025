from adodbapi.apibase import identity

with open("input.txt", "r") as file:
    input = file.read().split("\n")


total = 0
operation_total = 0
reduce_func = None
for i in range(max([len(i) for i in input])):
    try:
        if input[-1][i] != " ":
            total+=operation_total
        if input[-1][i] == "*":
            reduce_func = lambda x, y: x * y
            operation_total = 1
        if input[-1][i] == "+":
            reduce_func = lambda x, y: x + y
            operation_total = 0
    except IndexError:
        pass

    number = 0
    for j in range(len(input)-1):
        try:
            if input[j][i] != " ":
                number*=10
                number+=int(input[j][i])
        except IndexError:
            pass
    if number != 0:
        operation_total = reduce_func(operation_total, number)
total+=operation_total
print(total)