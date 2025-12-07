from functools import cache
from aoctools.Input import Input

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
beamcols = set()
currentcol = 0


@cache
def recursive(targetcol, row):
    if row >= len(task) - 1:
        return 1
    if task[row][targetcol] == "^":
        left = recursive(targetcol - 1, row + 1)
        right = recursive(targetcol + 1, row + 1)
        return left + right
    else:
        return recursive(targetcol, row + 1)


task = Input().get_input().splitlines()
for row, line in enumerate(task):
    for col, char in enumerate(line):
        if row == 0 and char == "S":
            start = (row, col)
            beamcols.add(col)
            currentcol = col
            continue
        if col in beamcols:
            if char == "^":
                ans += 1
                beamcols.remove(col)
                beamcols.add(col - 1)
                beamcols.add(col + 1)


print(ans)
print(recursive(currentcol, 0))
