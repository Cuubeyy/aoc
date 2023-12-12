from datetime import datetime
import os
import math
from get_input import GetInput
from itertools import combinations, groupby



def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        session = os.environ.get("AOC_SESSION")
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt").read()
    else:
        return open("test.txt").read()


def parse_data(inp1):
    data = get_input(inp1).splitlines()
    temp_data = []
    for i, l in enumerate(data):
        springs, conditions = l.split()
        springs = ((springs+"?")*5)[:-1]
        conditions = list(map(int, ((conditions + ",")*5)[:-1].split(",")))
        groups = ["".join(g) for k, g in groupby(springs)]#if k != '.']
        temp_data.append((conditions, springs, groups))
    return temp_data


def replacer(s, newstring, index):
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    return s[:index] + newstring + s[index + 1:]


def force(springs, conditions):
    temp = []
    springs = "".join(springs)
    for n in range(2 ** len(springs)):
        temp_springs = springs
        n = str(bin(n))[2:]
        n = n.zfill(len(springs))
        for index, b in enumerate(n):
            if b == "1":
                temp_springs = replacer(temp_springs, "#", index)
            else:
                temp_springs = replacer(temp_springs, ".", index)
        temp_lens = []
        temp_springs_2 = list(filter(None, temp_springs.split(".")))
        for t in temp_springs_2:
            temp_lens.append(len(t))
        if temp_lens == conditions:
            temp.append(temp_springs)
    return temp


start = datetime.now()
ans = 0
task = parse_data(False)
for line in task:
    temp_2 = []
    conditions, springs, groups = line
    print(groups)
    count = 0
    did = []
    for g in groups:
        count = g.count("#")
        temp = []
        if count > 0:
            i = conditions.index(count)
            before = groups[:i-1]
            groups = groups[i:]

            temp = [before, conditions[:i]]
            possible = force(temp[0], temp[1])
            temp_2.append(possible)

print(ans)
print(datetime.now() - start)
