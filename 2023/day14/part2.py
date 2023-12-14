from collections import defaultdict
from datetime import datetime
import os
import math
from get_input import GetInput

start = datetime.now()


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt").read()
    else:
        return open("test.txt").read()


def parse_data():
    global data
    data = get_input(False).splitlines()

    rocks = []
    cubes = []
    for y, l in enumerate(data):
        for x, ch in enumerate(l):
            if ch == "O":
                rocks.append([x, y])
            elif ch == "#":
                cubes.append([x, y])
    return rocks, cubes


def print_grid(rocks, cubes):
    return
    grid = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
    for r in rocks:
        grid[r[1]][r[0]] = "O"
    for c in cubes:
        grid[c[1]][c[0]] = "#"
    for l in grid:
        print("".join(l))
    print("="*len(data[0]))


data = []
dic = defaultdict(lambda: False)
ans = 0
rocks, cubes = parse_data()
rocks = sorted(rocks)
cycle = []
for n in range(1000000000):
    for i, rock in enumerate(rocks):
        x, y = rock
        stop = False
        if y == 0:
            stop = True
            dic[(x, y)] = True

        if not stop:
            for st in sorted(cubes, key=lambda x: (x[0], -x[1])):
                if st[0] != x:
                    if st[0] > x:
                        break
                    continue
                if st[1] > y:
                    continue
                y = st[1]+1
                while dic[(x, y)]:
                    y += 1
                rocks[i] = [x, y]
                dic[(x, y)] = True
                stop = True
                break
        if not stop:
            for r2 in sorted(rocks, key=lambda x: (x[0], -x[1])):
                if [x, y] == r2:
                    continue
                if r2[0] != x:
                    if r2[0] > x:
                        break
                    continue
                if r2[1] > y:
                    continue
                rocks[i] = [x, r2[1] + 1]
                stop = True
                break

        if not stop:
            rocks[i] = [x, 0]
            dic[(x, 0)] = True
    dic = defaultdict(lambda: False)
    rocks = sorted(rocks, key=lambda x: x[1])
    print_grid(rocks, cubes)
    for i, rock in enumerate(rocks):
        x, y = rock
        stop = False
        if x == 0:
            stop = True
            dic[(x, y)] = True

        if not stop:
            for st in sorted(cubes, key=lambda x: (x[1], -x[0])):
                if st[1] != y:
                    if st[1] > y:
                        break
                    continue
                if st[0] > x:
                    continue
                x = st[0]+1
                while dic[(x, y)]:
                    x += 1
                rocks[i] = [x, y]
                dic[(x, y)] = True
                stop = True
                break
        if not stop:
            for r2 in sorted(rocks, key=lambda x: (x[1], -x[0])):
                if [x, y] == r2:
                    continue
                if r2[1] != y:
                    if r2[1] > y:
                        break
                    continue
                if r2[0] > x:
                    continue
                rocks[i] = [r2[0]+1, y]
                dic[(r2[0]+1, y)] = True
                stop = True
                break

        if not stop:
            rocks[i] = [0, y]
            dic[(0, y)] = True
    dic = defaultdict(lambda: False)
    rocks = sorted(rocks, key=lambda x: (x[0], -x[1]))
    print_grid(rocks, cubes)
    for i, rock in enumerate(rocks):
        x, y = rock
        stop = False
        if y == len(data)-1:
            stop = True
            dic[(x, y)] = True

        if not stop:
            for st in sorted(cubes, key=lambda x: (x[0], x[1])):
                if st[0] != x:
                    if st[0] > x:
                        break
                    continue
                if st[1] < y:
                    continue
                y = st[1]-1
                while dic[(x, y)]:
                    y -= 1
                rocks[i] = [x, y]
                dic[(x, y)] = True
                stop = True
                break
        if not stop:
            for r2 in sorted(rocks, key=lambda x: (x[0], x[1])):
                if [x, y] == r2:
                    continue
                if r2[0] != x:
                    if r2[0] > x:
                        break
                    continue
                if r2[1] < y:
                    continue
                rocks[i] = [x, r2[1] - 1]
                stop = True
                break

        if not stop:
            rocks[i] = [x, len(data)-1]
            dic[(x, len(data)-1)] = True
    dic = defaultdict(lambda: False)
    rocks = sorted(rocks, key=lambda x: (x[1], -x[0]))
    print_grid(rocks, cubes)
    for i, rock in enumerate(rocks):
        x, y = rock
        stop = False
        if x == len(data[0])-1:
            stop = True
            dic[(x, y)] = True

        if not stop:
            for st in sorted(cubes, key=lambda x: x[1]):
                if st[1] != y:
                    if st[1] > y:
                        break
                    continue
                if st[0] < x:
                    continue
                x = st[0] - 1
                while dic[(x, y)]:
                    x -= 1
                rocks[i] = [x, y]
                dic[(x, y)] = True
                stop = True
                break
        if not stop:
            for r2 in sorted(rocks, key=lambda x: (x[1], x[0])):
                if [x, y] == r2:
                    continue
                if r2[1] != y:
                    if r2[1] > y:
                        break
                    continue
                if r2[0] < x:
                    continue
                rocks[i] = [r2[0] - 1, y]
                dic[(r2[0] - 1, y)] = True
                stop = True
                break

        if not stop:
            rocks[i] = [len(data[0])-1, y]
            dic[(len(data[0])-1, y)] = True
    print_grid(rocks, cubes)
    dic = defaultdict(lambda: False)
    rocks = sorted(rocks, key=lambda x: x[1])
    rocks = sorted(rocks)

    if rocks in cycle:
        cycle.append(sorted(rocks))
        break
    cycle.append(sorted(rocks))


before = cycle.index(rocks)
dist = n - before
print(before, dist)
# 3

print(cycle)

rocks = cycle[(1000000000%dist)-1]
for rock in rocks:
    ans += len(data) - rock[1]

with open(r'output1.txt', 'w') as fp:
    for item in cycle:
        fp.write("%s\n" % item)

print(ans)
print(datetime.now() - start)
# 99994 TOO LOW
