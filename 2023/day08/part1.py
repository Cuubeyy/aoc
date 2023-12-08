task = open("input.txt").read().splitlines()
network = {}
line_1 = task.pop(0)
task.pop(0)
for line in task:
    name, elements = line.split(" = ")
    element1 = elements.split(", ")[0][1:]
    element2 = elements.split(", ")[1][:-1]
    network[name] = [element1, element2, 0]
    (name, elements.split(", "))

step = "AAA"
count = 0
while step != "ZZZ":
    for instruction in line_1:
        count += 1
        if instruction == "L":
            step = network[step][0]
        else:
            step = network[step][1]
        if step == "ZZZ":
            break
print(count)
