import sys
from collections import defaultdict
from datetime import datetime
import os
import math
from functools import cache

start = datetime.now()
positions = set()

dic = {}
step_count = 0


def step(position, direction, count, path, heat):
    x, y, = position
    if x < 0 or y < 0:
        return
    elif x >= len(grid[0]) or y >= len(grid):
        return
    global step_count
    step_count += 1
    if step_count % 1000000 == 0:
        print(step_count, position, direction, count, len(dic), len(path), heat, min(h_min))
    if position in path:
        return
    key = (position, direction)
    if key in dic.keys():
        if heat >= dic[key]:
            return

    heat += int(grid[y][x])
    if position == (len(grid[0]) - 1, len(grid) - 1):
        if count > 3:
            print(heat)
            h_min.add(heat)
            return
    dic[key] = heat
    path.append(position)
    if count < 7:
        step((x + direction[0], y + direction[1]), direction, count + 1, path.copy(), heat)
    if count > 1:
        if abs(direction[0]) == 1:
            step((x, y + 1), (0, 1), 0, path.copy(), heat)
            step((x, y - 1), (0, -1), 0, path.copy(), heat)
        elif abs(direction[1]) == 1:
            step((x + 1, y), (1, 0), 0, path.copy(), heat)
            step((x - 1, y), (-1, 0), 0, path.copy(), heat)


ans = 0
h_min = set()
grid = open("test.txt").read().splitlines()
sys.setrecursionlimit(len(grid) ** 3)
step((0, 0), (1, 0), 0, [], -int(grid[0][0]))
print("-----\n", sorted(h_min)[0])
print(datetime.now() - start)

# 1545 False => Lower
