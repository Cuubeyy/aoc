import os
from aocd import get_data

if os.stat("input.txt").st_size == 0:
    session = "53616c7465645f5fd4c4e5a9c99eab4b32fd1c1cb75d89ee48af7c69048ac0f484e01eadece691272b1fc07b3617ae60624ef1e04c0acb3ca904d3cd62385204"
    data = get_data(session)
    with open("input.txt", "w") as f:
        f.write(data)

task = open("input.txt").read().splitlines()
forest = []

for i in task:
    temp = []
    for j in i:
        temp.append(int(j))
    forest.append(temp)


def lr(t, g, t_i):
    if (t == max(g[:t_i + 1]) and g[:t_i + 1].count(t) == 1) or (t == max(g[t_i:]) and g[t_i:].count(t) == 1):
        return True
    return False

ans = 0
trees = []
ans += len(forest[0]) * 2
for group_y in range(1, len(forest) - 1):
    group = forest[group_y]
    ans += 2
    for tree_x in range(1, len(group) - 1):
        tree = group[tree_x]
        if lr(tree, group, tree_x) or lr(tree, [forest[y][tree_x] for y in range(len(forest))], group_y):
            trees.append(tree)
print(trees)
print(len(trees) + ans)
