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
    return get_input(inp).splitlines()


def tilt_grid(grid_):
    free = defaultdict(lambda: 0)
    new_grid = [["." for _ in range(len(grid_[0]))] for _ in range(len(grid_))]
    for i, l in enumerate(grid_):
        for j, ch in enumerate(l):
            if ch == "#":
                free[j] = i + 1
                new_grid[i][j] = "#"
            elif ch == "O":
                y = free[j]
                new_grid[y][j] = "O"
                free[j] = y + 1
    return new_grid


def iterate(grid_):
    did_ = {}
    for n in range(1000000000):
        iteration = n + 1
        for i in range(4):
            grid_ = list(zip(*tilt_grid(grid_)[::-1]))
        if tuple(grid_) in did_:
            return iteration, did_, tuple(grid_)
        did_[tuple(grid_)] = iteration, grid_


n, did, last_config = iterate(parse_data(True))

before = did[last_config][0]
cycle_length = n - before
rest = 1000000000 - n
left_over = rest % cycle_length


map = []

for m in did:
    map.append(did[m])
map.sort()
grid = map[before + left_over-1][1]
ans = 0
for i, y in enumerate(grid):
    y = "".join(y)
    count = y.count("O")

    ans += (len(grid) - i) * count

print(ans)
print(datetime.now() - start)
