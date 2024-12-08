from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans = 0

task = Input().get_input().splitlines()


grid = TextGrid(task)
for t in task:
    t = list(t)
dict = defaultdict(list)
abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for ch in abc:
    patterns = grid.find_pattern_in_grid(ch)
    dict[ch].append(patterns)

pos = set()

for pattern in dict.values():
    pattern = pattern[0]
    for pos1 in pattern:
        for pos2 in pattern:
            if pos1 == pos2:
                continue
            dif = ((pos1[0] - pos2[0]), (pos1[1] - pos2[1]))
            poss = [pos1]
            pos.add(pos1)
            pos.add(pos2)
            for _ in range(len(task)**2):
                new_pos = (poss[-1][0] + dif[0], poss[-1][1] + dif[1])
                if not 0 <= new_pos[0] < len(task) or not 0 <= new_pos[1] < len(task[0]):
                    continue
                try:
                    if task[new_pos[0]][new_pos[1]]:
                        pos.add(new_pos)
                        poss.append(new_pos)
                except:
                    pass

print(sorted(list(pos)))
print(len(pos))
