from datetime import datetime
import os
import math
from itertools import groupby
from operator import itemgetter

from get_input import GetInput

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


def parse_data():
    blocks = []
    data = get_input(True).split("\n\n")
    for d in data:
        blocks.append(d.splitlines())
    return blocks



def check_mirror(image, line_index):
    smudge = 0
    for distance in range(line_index + 1):
        if line_index + 1 + distance >= len(image):
            return smudge == 1
        line1 = image[line_index + 1 + distance]
        line2 = image[line_index - distance]
        for ch_index, ch in enumerate(line1):
            if ch != line2[ch_index]:
                smudge += 1
                if smudge > 1:
                    return False
    return smudge == 1


ans = 0
blocks = parse_data()

for block in blocks:
    image = block
    for j in range(2):
        for i, line in enumerate(image):
            if i == len(image)-1:
                break
            value = check_mirror(image, i)
            if value and j == 0:
                ans += 100 * (i+1)
            elif value and j == 1:
                ans += i+1

        image = list(zip(*image[::-1]))
print(ans)
print(datetime.now() - start)
