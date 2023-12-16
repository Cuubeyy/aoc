import sys
from collections import defaultdict
from datetime import datetime
import os
import math
from functools import cache

from get_input import GetInput

sys.setrecursionlimit(110**2)

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


def parse_data(inp):
    data = get_input(inp).splitlines()
    return data




def step(matrix, movement, straid, pos, s):
    x, y, = pos
    if x < 0 or y < 0:
        return 0
    if x >= len(matrix[0]) or y >= len(matrix):
        return 0
    if dic[pos, movement, straid]:
        return 0
    dic[pos, movement, straid] = True
    positions.add(pos)
    ch = matrix[y][x]
    counter = 1
    if ch == '|':
        if movement:
            counter += step(matrix, False, False, (x, y - 1), s + 1)
            counter += step(matrix, False, True, (x, y + 1), s + 1)
        elif not movement:
            if straid:
                counter += step(matrix, False, True, (x, y + 1), s + 1)
            else:
                counter += step(matrix, False, False, (x, y - 1), s + 1)
    elif ch == '-':
        if not movement:
            counter += step(matrix, True, True, (x + 1, y), s + 1)
            counter += step(matrix, True, False, (x - 1, y), s + 1)
        elif movement:
            if straid:
                counter += step(matrix, True, True, (x + 1, y), s + 1)
            else:
                counter += step(matrix, True, False, (x - 1, y), s + 1)
    elif ch == "/":
        if movement:
            if straid:
                counter += step(matrix, False, False, (x, y - 1), s + 1)
            else:
                counter += step(matrix, False, True, (x, y + 1), s + 1)
        else:
            if straid:
                counter += step(matrix, True, False, (x - 1, y), s + 1)
            else:
                counter += step(matrix, True, True, (x + 1, y), s + 1)

    elif ch == "\\":
        if movement:
            if straid:
                counter += step(matrix, False, True, (x, y + 1), s + 1)
            else:
                counter += step(matrix, False, False, (x, y - 1), s + 1)
        else:
            if straid:
                counter += step(matrix, True, True, (x + 1, y), s + 1)
            else:
                counter += step(matrix, True, False, (x - 1, y), s + 1)
    elif ch == ".":
        if movement:
            if straid:
                counter += step(matrix, True, True, (x + 1, y), s + 1)
            else:
                counter += step(matrix, True, False, (x - 1, y), s + 1)
        else:
            if straid:
                counter += step(matrix, False, True, (x, y + 1), s + 1)
            else:
                counter += step(matrix, False, False, (x, y - 1), s + 1)

    return counter


task = parse_data(True)
m = []
for i in range(len(task)):
    positions = set()
    dic = defaultdict(bool)
    step(task, True, True, (0, i), 0)
    m.append(len(positions))
    positions = set()
    dic = defaultdict(bool)
    step(task, True, False, (len(task[0])-1, i), 0)
    m.append(len(positions))
for i in range(len(task[0])-1):
    positions = set()
    dic = defaultdict(bool)
    step(task, False, True, (i, 0), 0)
    m.append(len(positions))
    positions = set()
    dic = defaultdict(bool)
    step(task, False, False, (i, len(task[0])-1), 0)
    m.append(len(positions))

print(m)
print(max(m))

print(datetime.now() - start)
