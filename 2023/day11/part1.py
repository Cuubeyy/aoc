from datetime import datetime
import os
import math
from get_input import GetInput
import numpy as np

start = datetime.now()


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        session = os.environ.get("AOC_SESSION")
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
            f.close()
    if inp:
        return open("input.txt").read()
    else:
        return open("test.txt").read()


def parse_data():
    data = get_input(True).splitlines()

    galaxys = []
    empty_row = []
    empty_column = []

    for i, l in enumerate(data):
        if l.count("#") == 0:
            empty_row.append(i)
        else:
            for j, ll in enumerate(l):
                if ll == "#":
                    galaxys.append([j, i])

    for i in range(len(data[0])):
        p = True
        for j in range(len(data)):
            if data[j][i] == "#":
                p = False
        if p:
            empty_column.append(i)
    return sorted(empty_row), sorted(empty_column), sorted(galaxys, key=lambda x: x[1])


def get_pairs(galaxys):
    temp = []
    for i, g in enumerate(galaxys):
        for j, h in enumerate(galaxys[i + 1:]):
            temp.append((g, h))
    return temp


ans = 0
rows, columns, stars = parse_data()

for r in reversed(rows):
    for g in stars:
        if g[1] > r:
            g[1] += 1
for c in reversed(columns):
    for g in stars:

        if g[0] > c:
            g[0] += 1

pairs = get_pairs(stars)
for pair in pairs:
    p1, p2 = pair

    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    dMin = x + y
    ans += dMin

print(ans)
print(datetime.now() - start)
