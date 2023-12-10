import sys


def replacer(s, newstring, index, nofail=False):
    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring
    return s[:index] + newstring + s[index + 1:]


def find_loop(matrix, start, before, direction, step, loop):
    x, y = start
    char = matrix[y][x]
    n_x, n_y = x, y

    if before[1] > y:
        direction = -1
    elif before[1] < y:
        direction = 1
    elif before[0] > x:
        direction = -1
    else:
        direction = 1

    if step >= (len(matrix) * len(matrix[0])):
        return loop
    if char == "|":
        n_y += 1 * direction
    elif char == "-":
        n_x += 1 * direction
    elif char == "L":
        if before[0] > x:
            n_y = y - 1
            direction = -1
        elif before[1] < y:
            n_x = x + 1

    elif char == "J":
        if before[0] < x:
            n_y = y - 1
            direction = -1
        elif before[1] < y:
            n_x = x - 1
    elif char == "7":
        if before[0] < x:
            n_y = y + 1
        elif before[1] > y:
            n_x = x - 1
    elif char == "F":
        if before[0] > x:
            n_y = y + 1
        elif before[1] > y:
            n_x = x + 1
    elif char == ".":
        return loop
    elif char == "S":
        loop.append(start)
        return loop
    loop.append(start)
    return find_loop(matrix, (n_x, n_y), start, direction, step + 1, loop)


task = open("input.txt").read().splitlines()
sys.setrecursionlimit(len(task)*len(task[1])+1)
for y, line in enumerate(task):
    for x, pipe in enumerate(line):
        if pipe == 'S':
            start = x, y
            break

loop = find_loop(task, (int(start[0])+1, int(start[1])), start, 0, 0, [])
loop = sorted(loop)

for y, line in enumerate(task):
    open_pipe = 0
    for x, pipe in enumerate(line):
        if (x, y) not in loop:
            task[y] = replacer(task[y], ".", x)


counter = 0
direction = 0
for y, line in enumerate(task):
    open_pipe = 0
    for x, pipe in enumerate(line):
        if (x, y) not in loop:
            if open_pipe % 2 == 1:
                counter += 1

                task[y] = replacer(task[y], "#", x)
        else:
            if pipe != ".":
                try:
                    if pipe == "|":
                        open_pipe += 1
                        direction = 0
                    elif pipe == "-":
                        pass
                    elif pipe in ["J", "L", "S"]:
                        if direction == 1:
                            open_pipe += 1
                            direction = 0
                        elif direction == -1:
                            open_pipe += 2
                            direction = 0
                        elif direction == 0:
                            direction = -1
                    elif pipe in ["F", "7"]:
                        # print(direction)
                        if direction == 1:
                            open_pipe += 2
                            direction = 0
                        elif direction == -1:
                            open_pipe += 1
                            direction = 0
                        elif direction == 0:
                            direction = 1
                except:
                    pass
print(counter)
