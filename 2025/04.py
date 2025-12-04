from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1), (1, 1)]
ans1 = 0
ans2 = 0

task = Input().get_input().splitlines()
for i in range(len(task)):
    task[i] = list(task[i])


def checkNeighbours(x, y, grid):
    count = 0
    for dir in directions:
        try:
            ny, nx = y + dir[1], x + dir[0]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[y + dir[1]][x + dir[0]] == "@":
                    count += 1
        except:
            pass
    return count


for y, line in enumerate(task):
    for x, ch in enumerate(line):
        if ch == "@":
            if checkNeighbours(x, y, task) < 4:
                ans1 += 1


removed = True
while removed:
    removed = False
    for y, line in enumerate(task):
        for x, ch in enumerate(line):
            if ch == "@":
                if checkNeighbours(x, y, task) < 4:
                    ans2 += 1
                    removed = True
                    task[y][x] = "."
print(ans1, ans2)
