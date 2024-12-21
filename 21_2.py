from functools import cache
from itertools import combinations, permutations

import networkx as nx
from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0

# line by line input
task = Input().get_input().splitlines()
task = """029A
980A
179A
456A
379A""".splitlines()

keypad = """7 8 9
4 5 6
1 2 3
. 0 A""".splitlines()
keypad = [lines.split() for lines in keypad]
arrows = \
    """. ^ A
    < v >""".splitlines()
arrows = [lines.split() for lines in arrows]


def find(keys, key):
    for i, lines in enumerate(keys):
        if key in lines:
            return i, lines.index(key)


k_key = find(keypad, "A")
a_key = find(arrows, "A")


def solve(pos, sequence, keys):
    steps = []
    for ch in sequence:
        fpos = find(keys, ch)
        distance = (fpos[0] - pos[0], fpos[1] - pos[1])
        if distance[1] > 0:
            for _ in range(abs(distance[1])):
                steps.append(">")
        if distance[1] < 0:
            for _ in range(abs(distance[1])):
                steps.append("<")
        if distance[0] > 0:
            for _ in range(abs(distance[0])):
                steps.append("v")
        if distance[0] < 0:
            for _ in range(abs(distance[0])):
                steps.append("^")
        steps.append("A")
        pos = (pos[0] + distance[0], pos[1] + distance[1])
    return steps


@cache
def solve2(ch, pos):
    steps = []
    fpos = find(arrows, ch)
    distance = (fpos[0] - pos[0], fpos[1] - pos[1])
    if distance[1] > 0:
        for _ in range(abs(distance[1])):
            steps.append(">")
    if distance[1] < 0:
        for _ in range(abs(distance[1])):
            steps.append("<")
    if distance[0] > 0:
        for _ in range(abs(distance[0])):
            steps.append("v")
    if distance[0] < 0:
        for _ in range(abs(distance[0])):
            steps.append("^")
    steps.append("A")
    return steps


@cache
def rec(move: str, step: int) -> int:
    if step == 3:
        return move
    steps = solve2(move, a_key)
    ss = ""
    for s in steps:
        ss += rec(s, step+1)
    return ss


for line in task[:1]:
    steps = solve(k_key, line, keypad)
    print(steps)
    for step in steps:
        print(step, rec(step, 1))
