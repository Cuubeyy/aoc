from functools import cmp_to_key
from aoctools.Input import Input
from collections import defaultdict


ans1 = 0
ans2 = 0
p1 = True
dict = defaultdict(list)


def try_rule(rule):
    for i, n in enumerate(rule):
        for p in rule[i + 1:]:
            if p not in dict[n]:
                return False, i + 1
    return True, -1


def check(n1, n2):
    if n1 == n2:
        return 0
    if n1 in dict[n2]:
        return -1
    return 1


task = Input().get_input().splitlines()

for line in task:
    if line == "":
        p1 = False
        continue
    if not p1:
        x = list(map(int, line.split(",")))
        correct, error = try_rule(x)
        if correct:
            ans1 += x[len(x) // 2]
        else:
            x.sort(key=cmp_to_key(check))
            ans2 += x[len(x)//2]
    else:
        n1, n2 = list(map(int, line.split("|")))
        dict[n1].append(n2)

print(ans1)
print(ans2)
