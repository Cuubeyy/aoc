tasks = open("input.txt").read().splitlines()
ans = set()

hx, hy = (0, 4)
tx, ty = (0, 4)


def move_h(c, m):
    global hy, hx
    if m == "U":
        for i in range(c):
            hy -= 1
            move_t()
    if m == "D":
        for i in range(c):
            hy += 1
            move_t()
    if m == "L":
        for i in range(c):
            hx -= 1
            move_t()
    if m == "R":
        for i in range(c):
            hx += 1
            move_t()


def move_t():
    global tx, hx, ty, hy

    if ty == hy:
        if hx - tx > 1:
            tx += 1
        elif hx - tx < -1:
            tx -= 1
    elif tx == hx:
        if ty - hy > 1:
            ty -= 1
        elif ty - hy < -1:
            ty += 1
    elif ty != hy and tx != ty:
        if abs(abs(ty) - abs(hy)) > 1:
            if ty - hy < 0:
                ty += 1
                if tx - hx < 0:
                    tx += 1
                else:
                    tx -= 1
            elif ty - hy > 0:
                ty -= 1
                if tx - hx < 0:
                    tx += 1
                else:
                    tx -= 1
            else:
                print("!")
        elif abs(abs(tx) - abs(hx) > 1):
            if tx > hx:
                tx += 1
                if ty - hy < 0:
                    ty += 1
                else:
                    ty -= 1
            elif tx < hx:
                tx -= 1
                if ty - hy < 0:
                    ty += 1
                else:
                    ty -= 1
            else:
                print("!")
    if abs(hx - tx) > 1 or abs(hy - ty) > 1:
        print("H:", (hx + 1, hy + 1), "T:", (tx + 1, ty + 1))
    ans.add((tx, ty))


for task in tasks:
    m, c = task.split()
    c = int(c)
    move_h(c, m)
print(ans)
print(len(ans))

# 6076 too low
# 6098
# 7785 too high

# 2597
