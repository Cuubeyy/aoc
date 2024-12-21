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


def find(keys, key):
    for i, lines in enumerate(keys):
        if key in lines:
            return i, lines.index(key)


def process_sequence(sequence):
    results = ['']

    for item in sequence:
        if isinstance(item, str):
            results = [r + item for r in results]
        else:
            arrow_options = [''.join(tuple_item) for tuple_item in item]
            if len(arrow_options) == 1:
                results = [r + arrow_options[0] for r in results]
            else:
                new_results = []
                for result in results:
                    for option in arrow_options:
                        new_results.append(result + option)
                results = new_results

    return results


def solve(pos, sequence, keys):
    steps = []
    for ch in sequence:
        temp = []
        fpos = find(keys, ch)
        distance = (fpos[0] - pos[0], fpos[1] - pos[1])
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
        perms = list(set(permutations("".join(temp))))
        steps.append(perms)
        steps.append("A")
        pos = (pos[0] + distance[0], pos[1] + distance[1])
    return steps


for line in task:
    t = set()
    k_key = find(keypad, "A")
    a_key = find(arrows, "A")
    x = int(re.findall(r"\d+", line)[0])

    steps = solve(k_key, line, keypad)
    p_steps = process_sequence(steps)

    steps2 = solve(a_key, steps, arrows)
    p_steps2 = process_sequence(steps2)

    steps3 = solve(a_key, steps2, arrows)
    ans += min(t)

print(ans)
