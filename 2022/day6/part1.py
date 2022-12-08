import os
from aocd import get_data
from collections import Counter

if os.stat("input.txt").st_size == 0:
    session = "53616c7465645f5fd4c4e5a9c99eab4b32fd1c1cb75d89ee48af7c69048ac0f484e01eadece691272b1fc07b3617ae60624ef1e04c0acb3ca904d3cd62385204"
    data = get_data(session)
    with open("input.txt", "w") as f:
        f.write(data)

task = open("input.txt").read().splitlines()

found = False
ans = ""


def duplicated(input):
    WC = Counter(input)
    for letter, count in WC.items():
        if count > 1:
            return False
    return True


for j in range(len(task[0])):
    i = task[0][j]
    ans += i
    print(ans[-4:])
    if not duplicated(ans[-4:]) and not found:
        print("!")
        found = True
    if i not in ans[-4:-2] and found:
        string = "".join(ans[-4:])
        if duplicated(string):
            print(string, len(ans))
            exit()