from collections import defaultdict
from datetime import datetime
import os
import math
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
    data = get_input(True).split(",")

    return data


def calculate_number(label):
    count_ = 0
    for g in label:
        count_ += ord(g)
        count_ *= 17
        count_ = count_ % 256
    return count_

ans = 0
task = parse_data()
boxes = defaultdict(list)
for group in task:
    count = 0

    if "-" in group:
        label = group.split("-")[0]
        count = calculate_number(label)
        for i, b in enumerate(boxes[count]):
            if label == b[0]:
                boxes[count].pop(i)
                break
    elif "=" in group:
        label = group.split("=")[0]
        lens = group.split("=")[1]
        count = calculate_number(label)
        s = [label, lens]
        if len(boxes[count]) == 0:
            boxes[count].append(s)
        else:
            did = False
            for i, b in enumerate(boxes[count]):
                if label == b[0]:
                    boxes[count][i] = s
                    did = True
            if not did:
                boxes[count].append(s)

for index, b in enumerate(boxes):
    for s, slot in enumerate(boxes[b]):
        ans += ((b + 1) * (s+1) * int(slot[1]))
        print(((b + 1) * (s+1) * int(slot[1])))
print(ans)
print(datetime.now() - start)

# 346640 FALSE
