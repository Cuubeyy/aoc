from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys
import networkx as nx
sys.setrecursionlimit(1000000)

ans = 0
graph = nx.Graph()
# line by line input
task = Input().get_input().splitlines()

for line in task:
    c1, c2 = line.split("-")
    graph.add_edge(c1, c2)
subgraphs = list(nx.enumerate_all_cliques(graph))

print(",".join(sorted(subgraphs[-1])))

