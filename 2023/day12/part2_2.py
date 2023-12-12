import re
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
        groups = ["".join(g) for k, g in groupby(springs)]
        temp_data.append((conditions, springs, groups))
    return temp_data


start = datetime.now()
ans = 0
task = parse_data(False)
for line in task:
    temp_2 = []
    conditions, springs, groups = line

    print(groups)
    if "#"*max(conditions) in groups:
        for j in conditions:
            indexes = [i for i in range(len(groups)) if groups[i]=="#"*j]

            for index in indexes:
                try:
                    groups[index-1] = groups[index-1][:-1]+"."
                except IndexError: pass
                try:
                    groups[index+1] = "."+groups[index+1][1:]
                except IndexError: pass
    print(groups)

print(ans)
print(datetime.now() - start)
