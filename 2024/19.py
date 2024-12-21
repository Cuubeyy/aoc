from functools import cache

from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import networkx as nx
import sys

sys.setrecursionlimit(1000000)
graph = nx.DiGraph()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ans = 0

# line by line input
task = Input().get_input()

pattern, towels = task.split("\n\n")
towels = towels.splitlines()
pattern = pattern.split(", ")


@cache
def combine(st):
    if len(st) == 0:
        return 1
    a = 0
    for i, p in enumerate(pattern):
        if st.startswith(p):
            a += combine(st[len(p):])
    return a


for towel in towels:
    ans += combine(towel)
print(ans)
