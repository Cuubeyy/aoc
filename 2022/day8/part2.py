task = open("input.txt").read().splitlines()
forest = []

for i in task:
    temp = []
    for j in i:
        temp.append(int(j))
    forest.append(temp)


def lr(t, g, t_i):
    val = 1

    # left
    g_n = list(reversed(g[:t_i]))
    templ = 0
    for current in g_n:
        if current >= t:
            templ = g_n.index(current) + 1
            break
    if templ == 0:
        templ = len(g_n)
    val *= templ

    # right
    g_n = g[t_i + 1:]
    tempr = 0
    for current in g_n:
        if current >= t:
            tempr = g_n.index(current) + 1
            break
    if tempr == 0:
        tempr = len(g_n)
    val *= tempr

    return val


ans = 0
trees = []
ans += len(forest[0]) * 2
for group_y in range(1, len(forest) - 1):
    group = forest[group_y]
    ans += 2
    for tree_x in range(1, len(group) - 1):
        tree = group[tree_x]
        val = 1
        val *= lr(tree, group, tree_x)
        val *= lr(tree, [forest[y][tree_x] for y in range(len(forest))], group_y)
        trees.append(val)

print(trees)
print(max(trees))
