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
dir_map = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0), "A": (0, 0)}


def find(keys, key):
    for i, lines in enumerate(keys):
        if key in lines:
            return i, lines.index(key)


k_key = find(keypad, "A")
a_key = find(arrows, "A")

def find_next(pos, new_pos):
    temp = []
    distance = (- pos[0] + new_pos[0], - pos[1] + new_pos[1])
    if distance[1] > 0:
        for _ in range(abs(distance[1])):
            temp.append(">")
    if distance[1] < 0:
        for _ in range(abs(distance[1])):
            temp.append("<")
    if distance[0] > 0:
        for _ in range(abs(distance[0])):
            temp.append("v")
    if distance[0] < 0:
        for _ in range(abs(distance[0])):
            temp.append("^")
    temp.append("A")
    return temp

def valid(start, path):
    for point in path:
        start = (start[0] + dir_map[point][0], start[1] + dir_map[point][1])
    if task[start[0]][start[1]] == ".":
        return False
    return True

for line in task[:1]:
    pos = k_key
    seq = []
    for ch, ch2 in zip(line, line[1:]):
        p1 = find(keypad, ch)
        p2 = find(keypad, ch2)
        x = find_next(p1, p2)
        v = valid(p1, x)
        if not v:
            perms = permutations(x)
            for p in perms:
                v = valid(p1, p)
                if v:
                    x = p
                    break
        seq += x
    print(seq)
