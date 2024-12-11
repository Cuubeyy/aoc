from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans = 0


def search(prow, pcol, number, step, mstep, seen, path):
    if not 0 <= prow < len(task) or not 0 <= pcol < len(task[0]):
        return 0
    ch = task[prow][pcol]
    if ch == number:
        return 0
    if ch == "0" and step == mstep:
        path.append((prow, pcol))
        path = tuple(path)
        if path in seen:
            return 0
        seen.add(path)
        return 1
    if int(ch) - int(number) == -1:
        path.append((prow, pcol))
        c = 0
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            c += search(prow + d[0], pcol + d[1], ch, step + 1, mstep, seen, path.copy())
        return c
    return 0


task = Input().get_input().splitlines()

heads = set()

for irow in range(len(task)):
    for icol in range(len(task[0])):
        ch = task[irow][icol]
        if ch == "9":
            heads.add((irow, icol))

for srow, scol in heads:
    seen = set()
    x = search(srow, scol, "10", 0, 9, seen, [])
    print(x)
    ans += x
print(ans)
