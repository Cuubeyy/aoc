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


def parse_data(inp):
    global data
    data = get_input(inp).splitlines()

    rocks = []
    cubes = []
    for y, l in enumerate(data):
        for x, ch in enumerate(l):
            if ch == "O":
                rocks.append([x, y])
            elif ch == "#":
                cubes.append([x, y])
    return data, rocks, cubes


task = parse_data(False)

free = defaultdict(bool)

for i, l in enumerate(task):
    if i == 0:

    for j, ch in enumerate(l):

print(datetime.now() - start)
