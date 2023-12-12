from datetime import datetime
import os
import math
from get_input import GetInput
from itertools import combinations

start = datetime.now()


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
    for l in data:
        springs, conditions = l.split()
        conditions = conditions.split(",")
        temp_data.append((conditions, l))
    return temp_data


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


ans = 0
task = parse_data(True)
for line in task:
    conditions, springs = line
    count = 0
    unknown = [i for i, ltr in enumerate(springs) if ltr == "?"]
    did = []
    print(2**len(unknown))
    for n in range(2**len(unknown)):
        temp_springs = springs.split()[0]
        n = str(bin(n))[2:]
        n = n.zfill(len(unknown))
        for index, b in enumerate(n):
            if b == "1":
                temp_springs = replacer(temp_springs, "#", unknown[index])
            else:
                temp_springs = replacer(temp_springs, ".", unknown[index])
        temp_lens = []
        temp_springs = temp_springs.split(".")
        temp_springs = list(filter(None, temp_springs))
        for t in temp_springs:
            temp_lens.append(len(t))
        if temp_lens == list(map(int, conditions)):
            count+=1
    ans+=count

print(ans)
print(datetime.now() - start)
