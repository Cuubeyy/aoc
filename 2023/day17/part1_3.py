import sys
from collections import defaultdict
from datetime import datetime
import os
import math
from functools import cache
from collections import deque


start = datetime.now()
positions = set()

dic = {}


def step(position, direction, count, path, heat):
    step_count = 0
    queue = deque([])
    key = (position, direction, count, heat)
    queue.append(key)
    while queue:
        step_count += 1
        position, direction, count, heat = queue.popleft()
        key1 = (position, direction, count)
        if step_count % 1000000 == 0:
            print(step_count, position, direction, count, len(dic), len(path), heat)

        x, y = position
        if x < 0 or y < 0:
            continue
        elif x >= len(grid[0]) or y >= len(grid):
            continue

        heat += int(grid[y][x])
        if key1 in dic.keys():
            if heat >= dic[key1]:
                continue

        if h_min:
            if heat >= min(h_min):
                continue

        if position == (len(grid[0]) - 1, len(grid) - 1):
            if count > 2:
                h_min.add(heat)
            continue


        dic[key1] = heat
        if count < 9:
            queue.append(((x + direction[0], y + direction[1]), direction, count + 1, heat))
        if count > 2:
            if abs(direction[0]) == 1:
                queue.append(((x, y + 1), (0, 1), 0, heat))
                queue.append(((x, y - 1), (0, -1), 0, heat))
            elif abs(direction[1]) == 1:
                queue.append(((x + 1, y), (1, 0), 0, heat))
                queue.append(((x - 1, y), (-1, 0), 0, heat))


ans = 0
h_min = set()
grid = open("test.txt").read().splitlines()
sys.setrecursionlimit(len(grid) ** 3)
step((0, 0), (1, 0), 0, [], -int(grid[0][0]))
print("-----\n", min(h_min))
print(datetime.now() - start)

# 1324 TOO HIGH
