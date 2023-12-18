from datetime import datetime
import os
import math
from get_input import GetInput

start = datetime.now()


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        session = os.environ.get("AOC_SESSION")
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt").read()
    else:
        return open("test2.txt").read()


def parse_data():
    data = get_input(False).splitlines()
    temp = []
    for l in data:
        direction, amount, color = l.split()
        amount = int(amount)
        color = color[1:-1]
        temp.append((direction, amount, color))
    return temp


def area(vs):
    a = 0
    x0, y0 = vs[0]
    for [x1, y1] in vs[1:]:
        dx = x1-x0
        dy = y1-y0
        a += 0.5*(y0*dx - x0*dy)
        x0 = x1
        y0 = y1
    return a


def fill_map(m_, positions_):
    for p_ in positions_:
        m_[p_[1]][p_[0]] = "#"
    return m_


task = parse_data()
positions = []
x_min = math.inf
y_min = math.inf
x_max = 0
y_max = 0
directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
position = [100, 100]
ans = 0
positions.append(position)
for direction, amount, color in task:
    direction = directions[direction]
    x, y = position
    for i in range(amount):
        x += direction[0]
        y += direction[1]
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
        position = [x, y]
        positions.append(position)
positions.pop(-1)
for i, (x, y) in enumerate(positions):
    positions[i][0] -= x_min
    positions[i][1] -= y_min
last_y = 0
last_x = 0
volume = 0
print(x_max, x_min, y_max, y_min)
map = [["." for _ in range(x_max - x_min+1)] for _ in range(abs(y_max - y_min+1))]
map = fill_map(map, positions)
for m in map:
    print("".join(m))
did = False
positions.sort(key=lambda x: (x[1], x[0]))
print(area(positions))
print(volume + len(positions))
print(datetime.now() - start)

# 65098 TOO HIGH
# 65097 TOO HIGH
# 52748 TOO HIGH
