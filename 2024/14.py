import time

from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans = defaultdict(int)

task = Input().get_input().splitlines()
space = (101, 103)
for i in range(999999):
    robots = []
    picture = [[" " for __ in range(101)] for _ in range(103)]
    for line in task:
        p,v = line.split()
        p = list(map(int, p[2:].split(",")))
        v = list(map(int, v[2:].split(",")))

        p1, p2 = p
        v1, v2 = v

        p1 = p1 + v1 * i
        p2 = p2 + v2 * i
        p1, p2 = p1 % space[0], p2 % space[1]
        robots.append((p1, p2))
        picture[p2][p1] = "█"

    if all(robots.count(j) == 1 for j in robots):
        for p in picture:
            print("".join(p))
        print(i)
        print("--------------------------------")
        input()
