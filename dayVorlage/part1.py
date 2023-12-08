import os
from aocd import get_data

if os.stat("input.txt").st_size == 0:
    session = os.environ.get("AOC_SESSION")
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
