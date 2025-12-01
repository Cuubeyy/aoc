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
for line in task:
    pass

# one line input
task = Input().get_input()
for char in task:
    pass

# grid_input
task = Input().get_input()
grid = TextGrid(task)
print(grid)
