import os
from aocd import get_data

if os.stat("input.txt").st_size == 0:
    session = "53616c7465645f5fd4c4e5a9c99eab4b32fd1c1cb75d89ee48af7c69048ac0f484e01eadece691272b1fc07b3617ae60624ef1e04c0acb3ca904d3cd62385204"
    data = get_data(session)
    with open("input.txt", "w") as f:
        f.write(data)

task = open("input.txt").read().splitlines()
ans = ""

l = 0

stacks = []
rows = []
anweisungen = []

for line in task:
    if "1" in line:
        line = line.split()
        l = int(max(line))
        break
    rows.append(line.split())

for i in range(l):
    stacks.append([])

for i in range(len(stacks)):
    s = stacks[i]
    for j in rows:
        s.append(j[i])

for line in task:
    if "move" in line:
        line = line.replace("from", "")
        line = line.replace("to", "")
        anweisungen.append(line.replace("move", "").split())

for s in stacks:
    if "..." in s:
        x = s.count("...")
        for y in range(x):
            s.remove("...")
    s.reverse()

for a in anweisungen:
    amount = int(a[0])
    position = int(a[1])-1
    target = int(a[2])-1

    for i in range(amount):
        stacks[target].append(stacks[position].pop(-amount+i))

for s in stacks:
    ans += s[-1]
ans = ans.replace("[", "")
ans = ans.replace("]", "")
print(ans)