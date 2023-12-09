import math

task = open("input.txt").read().splitlines()
ans = 0
network = {}
network_2 = []
line_1 = task.pop(0)
task.pop(0)
for line in task:
    name, elements = line.split(" = ")
    element1 = elements.split(", ")[0][1:]
    element2 = elements.split(", ")[1][:-1]
    (name, elements.split(", "))
    if name.endswith("A"):
        network_2.append(name)

z_repeat = []
for index, s in enumerate(network_2):
    step = s
    count = 0
    z = ()
    while not z:
        for instruction in line_1:
            if step.endswith("Z") and not z:
                z = count
                break
            if instruction == "L":
                step = network[step][0]
            else:
                step = network[step][1]
            count += 1
    z_repeat.append(z)

print(math.lcm(*z_repeat))
