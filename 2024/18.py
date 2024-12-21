from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys
import networkx as nx

sys.setrecursionlimit(1000000)


def test():
    graph = nx.DiGraph()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for irow, row in enumerate(grid):
        for icol, col in enumerate(row):
            if row == "#":
                continue
            for dr, dc in directions:
                nr, nc = irow + dr, icol + dc
                if 0 <= nr < 71 and 0 <= nc < 71 and grid[nr][nc] == ".":
                    graph.add_edge((irow, icol), (nr, nc))

    return nx.shortest_path_length(graph, (0, 0), (70, 70))


ans = 0
# line by line input
grid = []
task = Input().get_input().splitlines()

for _ in range(71):
    t = []
    for __ in range(71):
        t.append(".")
    grid.append(t)
i = 1000
while True:
    line = task[i]
    x, y = list(map(int, line.split(",")))
    grid[y][x] = "#"
    try:
        test()
    except:
        print(line)
        break
    i += 1

for g in grid:
    print("".join(g))

