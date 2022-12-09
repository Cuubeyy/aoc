tasks = open("input.txt").read().splitlines()
ans = set()

hx, hy = (0, 0)
tx, ty = (0, 0)

dic = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def move_h(c, m):
    global hy, hx
    for i in range(c):
        print("H:", (hx, hy), "T:", (tx, ty))
        move = dic[m]
        hx += move[0]
        hy += move[1]
        print("H:", (hx, hy), "T:", (tx, ty))
        move_t()
        print("H:", (hx, hy), "T:", (tx, ty), "\n")


def move_t():
    global tx, hx, ty, hy
    if tx+1 < hx:
        tx += 1
        if ty < hy:
            ty += 1
        elif ty > hy:
            ty -= 1
    elif tx-1 > hx:
        tx -= 1
        if ty < hy:
            ty += 1
        elif ty > hy:
            ty -= 1

    elif ty+1 < hy:
        ty += 1
        if tx < hx:
            tx += 1
        elif tx > hx:
            tx -= 1
    elif ty-1 > hy:
        ty -= 1
        if tx < hx:
            tx += 1
        elif tx > hx:
            tx -= 1

    ans.add((tx, ty))


for task in tasks:
    m, c = task.split()
    c = int(c)
    move_h(c, m)
print(ans)
print(len(ans))
