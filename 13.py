from functools import cache
from sympy import symbols, Eq, solve, Integer
from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(10000**2)
ans = 0

# line by line input
task = Input().get_input().splitlines()

groups = []
group = []
c = 0
for line in task:
    if line == "":
        groups.append(group)
        group = []
        c = 0
        continue
    elif c != 2:
        button, values = line.split(": ")
        a, b = values.split(", ")
        a = int(a[1:])
        b = int(b[1:])
        group.append((a, b))
        c += 1
    else:
        _, values = line.split(": ")
        x, y = values.split(", ")
        x = int(x[2:]) + 10000000000000
        y= int(y[2:]) + 10000000000000
        group.append((x, y))

for group in groups:
    x, y = symbols("x,y")
    def makeeq(grou):
        eq1 = Eq(grou[2][0], x * grou[0][0] + y*grou[1][0])
        eq2 = Eq(grou[2][1], x * grou[0][1] + y*grou[1][1])
        return eq1, eq2
    rq1, rq2 = makeeq(group)
    solved = solve((rq1, rq2), (x, y))
    if not solved[x].is_Integer and not solved[y].is_Integer:
        continue
    c = solved[x] * 3 + solved[y]
    if c.is_Integer:
        ans += c
print(ans)