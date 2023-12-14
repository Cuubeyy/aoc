from collections import defaultdict
from datetime import datetime
import os
import math
from get_input import GetInput

start = datetime.now()


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt").read()
    else:
        return open("test.txt").read()


def parse_data():
    global data
    data = get_input(True).splitlines()

    rocks = []
    cubes = []
    for y, l in enumerate(data):
        for x, ch in enumerate(l):
            if ch == "O":
                rocks.append([x, y])
            elif ch == "#":
                cubes.append([x, y])
    return rocks, cubes


dic = defaultdict(lambda: False)
data = []
ans = 0
rocks, cubes = parse_data()
rocks = sorted(rocks)
for i, rock in enumerate(rocks):
    x, y = rock
    stop = False
    if y == 0:
        stop = True
        dic[(x, y)] = True

    if not stop:
        for st in sorted(cubes, key=lambda x: (x[0], -x[1])):
            if st[0] != x:
                if st[0] > x:
                    break
                continue
            if st[1] > y:
                continue
            y = st[1]+1
            while dic[(x, y)]:
                y += 1
            rocks[i] = [x, y]
            dic[(x, y)] = True
            stop = True
            break
    if not stop:
        for r2 in sorted(rocks, key=lambda x: (x[0], -x[1])):
            if [x, y] == r2:
                continue
            if r2[0] != x:
                if r2[0] > x:
                    break
                continue
            if r2[1] > y:
                continue
            rocks[i] = [x, r2[1] + 1]
            stop = True
            break

    if not stop:
        rocks[i] = [x, 0]
        dic[(x, 0)] = True

    ans += len(data) - rocks[i][1]

print(ans)
print(datetime.now() - start)
