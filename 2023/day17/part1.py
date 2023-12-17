import sys
from datetime import datetime
import os
import math
from functools import cache

from get_input import GetInput

start = datetime.now()


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        session = os.environ.get("AOC_SESSION")
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt").read()
    else:
        return open("test.txt").read()


def parse_data():
    data = get_input(False).splitlines()
    return data


dic = {}
positions = set()


def step(position, direction, direction_count, steps, heats):
    global task
    x, y = position
    if x >= len(task[0]) or y >= len(task):
        return False
    elif x < 0 or y < 0:
        return False
    heat = int(task[y][x])
    if position in steps:
        return False
    steps.append((x, y))
    heats.append(heat)
    positions.add(position)
    if position == (len(task[0]) - 1, len(task) - 1):
        print(steps)
        print(sum(heats))
        return True
    if direction_count >= 3:
        if abs(direction[0]) == 1:
            step((x, y + 1), (0, 1), 0, steps.copy(), heats)
            step((x, y - 1), (0, -1), 0, steps.copy(), heats)
        else:
            step((x + 1, y), (1, 0), 0, steps.copy(), heats)
            step((x - 1, y), (-1, 0), 0, steps.copy(), heats)
    elif direction_count < 3:
        step((x + direction[0], y + direction[1]), direction, direction_count + 1, steps.copy(), heats)
        if abs(direction[0]) == 1:
            step((x, y + 1), (0, 1), 0, steps.copy(), heats)
            step((x, y - 1), (0, -1), 0, steps.copy(), heats)
        else:
            step((x + 1, y), (1, 0), 0, steps.copy(), heats)
            step((x - 1, y), (-1, 0), 0, steps.copy(), heats)


ans = 0
task = parse_data()
sys.setrecursionlimit(len(task) ** 2)
ans = step((0, 0), (1, 0), 0, [], [])
print(positions)
print(ans)
print(datetime.now() - start)
