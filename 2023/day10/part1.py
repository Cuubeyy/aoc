import sys
from datetime import datetime
import os
from aocd import get_data
import math


def find_loop(matrix, start, before, direction, step, loop):
    # start = (0, 0)
    x, y = start
    char = matrix[y][x]
    n_x, n_y = x, y

    if before[1] > y:
        direction = -1
    elif before[1] < y:
        direction = 1
    elif before[0] > x:
        direction = -1
    else:
        direction = 1

    if step >= (len(matrix) * len(matrix[0])):
        return loop
    if char == "|":
        n_y += 1 * direction
    elif char == "-":
        n_x += 1 * direction
    elif char == "L":
        if before[0] > x:
            n_y = y - 1
            direction = -1
        elif before[1] < y:
            n_x = x + 1

    elif char == "J":
        if before[0] < x:
            n_y = y - 1
            direction = -1
        elif before[1] < y:
            n_x = x - 1
    elif char == "7":
        if before[0] < x:
            n_y = y + 1
        elif before[1] > y:
            n_x = x - 1
    elif char == "F":
        if before[0] > x:
            n_y = y + 1
        elif before[1] > y:
            n_x = x + 1
    elif char == ".":
        return loop
    elif char == "S":
        loop.append("S")
        return loop
    loop.append(start)

    return find_loop(matrix, (n_x, n_y), start, direction, step + 1, loop)


task = open("input.txt").read().splitlines()
ans = 0
sys.setrecursionlimit(len(task)*len(task[1])+1)
for y, line in enumerate(task):
    for x, pipe in enumerate(line):
        if pipe == 'S':
            start = x, y
            break

loop = find_loop(task, (int(start[0])+1, int(start[1])), start, 0, 0, [])
ans = int(len(loop)/2)
print(ans)
