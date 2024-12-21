from functools import cache

from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

task = Input().get_input().splitlines()

grid = TextGrid(task)

start = grid.find_pattern_in_grid("S")[0]
end = grid.find_pattern_in_grid("E")[0]
walls = grid.find_pattern_in_grid("#")
path = grid.find_pattern_in_grid(".")

paths = set()


def fs(col, row, step, saw):
    c = 0
    if (col, row) in saw:
        return False, saw
    saw.append((col, row))
    ch = task[col][row]
    if ch == "E":
        return True, saw
    for dir in directions:
        new_col, new_row = col + dir[0], row + dir[1]
        if 0 <= new_col < len(task) and 0 <= new_row < len(task[0]):
            if task[new_col][new_row] == "." or task[new_col][new_row] == "E":
                t, x = fs(new_col, new_row, step + 1, saw)
                if t:
                    return True, x
    return False, saw


seen = fs(start[0], start[1], 0, [])[1]
for i, (col, row) in enumerate(seen):
    for j, (ncol, nrow) in enumerate(seen):
        distance = (abs(col - ncol), abs(row - nrow))
        if sum(distance) <= 20:
            saved = (len(seen) - 1) - j + i + sum(distance)
            if saved < len(seen) - 100:
                ans += 1
print(ans)

# 1023067 too high
# 1018892 too high
