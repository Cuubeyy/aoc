task = open("test2.txt").read().splitlines()
ans = 0
network = {}
network_2 = []
did = []
line_1 = task.pop(0)
task.pop(0)
for line in task:
    name, elements = line.split(" = ")
    element1 = elements.split(", ")[0][1:]
    element2 = elements.split(", ")[1][:-1]
    network[name] = [element1, element2, 0]
    (name, elements.split(", "))
    network_2.append([name, (element1, element2)])

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
