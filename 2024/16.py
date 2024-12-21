import datetime
from aoctools.Input import Input
import networkx as nx
import matplotlib.pyplot as plt

starttime = datetime.datetime.now()
ans = 0

task = Input().get_input().splitlines()

task = [list(line) for line in task]
graph = nx.DiGraph()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for irow, row in enumerate(task):
    for icol, col in enumerate(row):
        if col == "#":
            continue
        if col == "S":
            start = (irow, icol)
        elif col == "E":
            end = (irow, icol)
        elif col == ".":
            for d in range(4):

                graph.add_edge((irow, icol))


for node, dir in graph.nodes:
    if dir == 0:
        dest = (node[0]-1, node[1])
    elif dir == 1:
        dest = (node[0], node[1]+1)
    elif dir == 2:
        dest = (node[0]+1, node[1])
    elif dir == 3:
        dest = (node[0], node[1]-1)

    if (dest, dir) in graph.nodes:
        graph.add_edge((node, dir), (dest, dir), weight=1)

    for ndir in range(4):
        graph.add_edge((node, dir), (node, ndir), weight=1000)

for dir in range(4):
    graph.add_edge((end, dir), "end", weight=0)
    graph.add_edge("start", (start, dir), weight=0)

length = nx.dijkstra_path_length(graph, (start, 0), "end")+1000
print(length)
paths = nx.all_shortest_paths(graph, (start, 2), "end", weight="weight")

nodes = set()
for path in paths:
    for node in path:
        if node != "end":
            nodes.add(node[0])

answer = len(nodes)
print(len(nodes))
print(datetime.datetime.now() - starttime)
