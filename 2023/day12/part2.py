import re
import sys
from datetime import datetime
import os
import math
from get_input import GetInput
from itertools import combinations, groupby
from functools import cache


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        session = os.environ.get("AOC_SESSION")
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt")
    else:
        return open("test.txt")


def parse_data(inp1):
    temp_data = []
    data = get_input(inp1).readlines()
    for line in data:
        line = line.strip()
        springs, conditions = line.split()

        springs = "?".join([springs] * 5)
        conditions = tuple(int(x) for x in conditions.split(",")) * 5

        temp_data.append((springs, conditions))

    return temp_data


@cache
def solve(springs: str, conditions: tuple[int]) -> int:
    if len(springs) == 0:
        if len(conditions) == 0:
            return 1
        return 0

    if len(conditions) == 0:
        if "#" in springs:
            return 0
        return 1

    counter = 0
    if springs[0] in [".", "?"]:
        counter += solve(springs[1:], conditions)

    if springs[0] in ["#", "?"]:
        if conditions[0] <= len(springs) and "." not in springs[:conditions[0]]:
            if conditions[0] == len(springs) or springs[conditions[0]] != "#":
                counter += solve(springs[conditions[0] + 1:], conditions[1:])

    return counter


start = datetime.now()
ans = 0
task = parse_data(True)
for springs, counts in task:
    ans += solve(springs, counts)
print(ans)
print(datetime.now() - start)
