task = open("03.in").read()

ans = 0
numbers = []
x, y = 0, 0
x1, y1 = 0, 0

coords = set()

for i, line in enumerate(task):
    if i % 2 == 1:
        if line == "^":
            y1 += 1
        elif line == "<":
            x1 -= 1
        elif line == ">":
            x1 += 1
        elif line == "v":
            y1 -= 1
        coords.add((x1, y1))

    if i % 2 == 0:
        if line == "^":
            y += 1
        elif line == "<":
            x -= 1
        elif line == ">":
            x += 1
        elif line == "v":
            y-=1
        coords.add((x, y))

print(len(coords))
