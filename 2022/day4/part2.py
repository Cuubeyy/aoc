import os
from aocd import get_data

if os.stat("input.txt").st_size == 0:
    session = "53616c7465645f5fd4c4e5a9c99eab4b32fd1c1cb75d89ee48af7c69048ac0f484e01eadece691272b1fc07b3617ae60624ef1e04c0acb3ca904d3cd62385204"
    data = get_data(session)
    with open("input.txt", "w") as f:
        f.write(data)

task = open("input.txt").read().splitlines()
ans = 0


def compare(part1, part2):
    part1 = list(map(int, part1))
    part2 = list(map(int, part2))

    for i in range(part1[0], part1[1]+1):
        if i in range(part2[0], part2[1]+1):
            return True


for i in task:
    part1, part2 = i.split(",")
    part1 = part1.split("-")
    part2 = part2.split("-")

    if compare(part1, part2):
        print(part1, part2)
        ans += 1

print(ans)
