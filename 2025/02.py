from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
ans2 = 0


def isValid(id):
    id1 = str(id)[:len(str(id))//2]
    id2 = str(id)[len(str(id))//2:]
    if id1 == id2:
        return False
    return True


def isValid2(id):
    newID = ""
    id = str(id)
    originID = id
    for i in range(0, len(str(id)) - 1):
        newID += id[0]
        id = id[1:]

        if (id.count(newID) + 1) * len(str(newID)) == len(str(originID)):
            return False
    return True

# one line input
task = Input().get_input()
for ids in task.split(","):
    fist, last = ids.split("-")
    for i in range(int(fist), int(last) + 1):
        if not isValid(i):
            ans += int(i)
        if not isValid2(i):
            ans2 += int(i)
print(ans)
print(ans2)
