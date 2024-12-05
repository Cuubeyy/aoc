import functools
from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans1 = 0
ans2 = 0

r1 = set()
r2 = []

p1 = True
dict = defaultdict(list)


def try_rule(rule):
    for i, n in enumerate(rule):
        for p in rule[i + 1:]:
            if p not in dict[n]:
                return False, i + 1
    return True, -1


def sort(rule, sorte):
    if len(rule) == 0:
        return True, sorte
    for i, n in enumerate(rule):
        if try_rule(list(sorte) + [n])[0]:
            rule_n = list(rule).copy()
            rule_n.pop(i)
            fit, n_sort = sort(tuple(rule_n), tuple(list(sorte) + [n]))
            if fit:
                return True, n_sort

    return False, sorte


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
            x.sort(key=functools.cmp_to_key(check))
            ans2 += x[len(x)//2]
    else:
        n1, n2 = list(map(int, line.split("|")))
        r1.add((n1, n2))
        dict[n1].append(n2)

print(ans1)
print(ans2)
