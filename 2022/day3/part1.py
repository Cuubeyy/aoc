import os
from aocd import get_data

if os.stat("input.txt").st_size == 0:
    session = "53616c7465645f5fd4c4e5a9c99eab4b32fd1c1cb75d89ee48af7c69048ac0f484e01eadece691272b1fc07b3617ae60624ef1e04c0acb3ca904d3cd62385204"
    data = get_data(session)
    with open("input.txt", "w") as f:
        f.write(data)

task = open("input.txt").read().splitlines()
ans = 0

sol = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
       "S", "T", "U", "V", "W", "X", "Y", "Z"]


def compare(part1, part2):
    for j in part1:
        if j in part2:
            return sol.index(j) + 1


for i in task:
    part1 = i[slice(0, len(i) // 2)]
    part2 = i[slice(len(i) // 2, len(i))]

    ans += compare(part1, part2)

print(ans)