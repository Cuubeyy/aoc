import os
from aocd import get_data

if os.stat("input.txt").st_size == 0:
    session = "53616c7465645f5fd4c4e5a9c99eab4b32fd1c1cb75d89ee48af7c69048ac0f484e01eadece691272b1fc07b3617ae60624ef1e04c0acb3ca904d3cd62385204"
    data = get_data(session)
    with open("input.txt", "w") as f:
        f.write(data)

task = open("input.txt").read().splitlines()
ans = 0

for i in task:
    if i == '':
        continue
    ans += int(i)

print(ans)