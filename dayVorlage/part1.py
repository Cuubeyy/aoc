import os
from aocd import get_data

if os.stat("input.txt").st_size == 0:
    session = "53616c7465645f5f0fee3a4adba2d4850f273dec46cc7a411debbc92dcd73989d552fb397854b3819375fe33e3221345dfd1f70c3b4357549a127747ba19f5e3"
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