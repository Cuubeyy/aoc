from math import lcm

import numpy as np

task = open("input.txt").read().splitlines()
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
    if name.endswith("A"):
        network_2.append(name)

print(network_2)
counter = 0
start_steps = []
for s in network_2:
    step = s
    counter = 0
    while not step.endswith("Z"):
        for instructions in line_1:
            counter += 1
            if instructions == "L":
                step = network[step][0]
            else:
                step = network[step][1]
            if step.endswith("Z"):
                break
    start_steps.append(counter)


print(lcm(*start_steps))
