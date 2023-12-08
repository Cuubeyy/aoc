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

z_repeat = []
print(network_2)
for index, s in enumerate(network_2):
    did = set()
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
print(z_repeat)

ans = 1
count = 111129309
while True:
    temp = max(z_repeat)*count
    p = []
    for x in z_repeat:
        if temp % x == 0:
            p.append(True)
        else:
            p.append(False)
    print(temp, count, p)
    if all(p):
        break
    count += 1
print(temp)

# 144822660 TOO LOW
# 1033041428962339627 TOO HIGH

