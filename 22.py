from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans = 0

def mix(n, x):
    return n ^ x

def prune(n):
    return n % 16777216


task = Input(22).get_input().splitlines()
task = """1
2
3
2024""".splitlines()
def calc_secret(number):
    secret = number
    s = secret * 64
    secret = prune(mix(s, secret))

    s = secret // 32
    secret = prune(mix(s, secret))

    s = secret * 2048
    secret = prune(mix(s, secret))
    return secret

for line in task:
    number = int(line)
    numbers = []
    valid = set()
    for _ in range(2000):
        number = calc_secret(number)
        numbers.append(int(str(number)[-1]))
    new = [x1- x2 for x1, x2 in zip(numbers, numbers[1:])]
    changed = 0
    for i, n1 in enumerate(new):
        if i == 0:
            changed = 1
            continue
        if new[i-1] == n1:
            changed = 0
        else:
            changed += 1
        if changed > 4:
            valid.add(numbers[i])
    print(valid)
    ans += max(valid)
print(ans)
