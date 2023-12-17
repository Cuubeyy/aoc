import sys
from collections import defaultdict
from datetime import datetime
import os
import math
from functools import cache

start = datetime.now()
positions = set()


def calculate_heat(path):
    if len(path) == 0:
        return
    d = 0
    for p in path:
        d += int(grid[p[1]][p[0]])
    print(d)


dic = defaultdict(lambda: False)


def step(position, direction, count, path):
    key = tuple((tuple(path), direction))
    if position in path:
        return
    if key in dic:
        return
    x, y, = position
    if x < 0 or y < 0:
        return
    elif x >= len(grid) or y >= len(grid):
        return
    if position == (len(grid[0]) - 1, len(grid) - 1):
        calculate_heat(path)
        return
    dic[key] = True
    path.add(position)
    if count < 3:
        step((x + direction[0], y + direction[1]), direction, count + 1, path.copy())
    if abs(direction[0]) == 1:
        step((x, y + 1), (0, 1), 0, path.copy())
        step((x, y - 1), (0, -1), 0, path.copy())
    elif abs(direction[1]) == 1:
        step((x + 1, y), (1, 0), 0, path.copy())
        step((x - 1, y), (-1, 0), 0, path.copy())


ans = 0
grid = open("test.txt").read().splitlines()
sys.setrecursionlimit(len(grid) ** 5)
step((0, 0), (1, 0), 0, set())
print(grid)
print(datetime.now() - start)
