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


grid = parse_data(True)
grid = tilt_grid(grid)

ans = 0
for i, y in enumerate(grid):
    y = "".join(y)
    count = y.count("O")

    for _ in range(count):
        ans += len(grid[0]) - i

print(ans)
print(datetime.now() - start)
