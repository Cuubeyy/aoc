tasks = open("input.txt").read().splitlines()
ans = set()


class Node:
    def __init__(self, number, pos):
        self.number = number
        self.position = pos

    def __str__(self):
        return "number: " + str(self.number) + ", position: " + str(self.position)


hx, hy = (0, 0)

nodes = []
for i in range(1, 9 + 1):
    nodes.append(Node(i, (0, 0)))

dic = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def move_h(c, m):
    global hy, hx
    before = None
    for i in range(c):
        move = dic[m]
        hx += move[0]
        hy += move[1]
        before = (hx, hy)
        print("number:", 0, "position:", before)
        for n in nodes:
            n.position = move_node(before, n.position)
            print(n)
            before = n.position
        ans.add(before)
        print("\n")



def move_node(h, t):
    hx, hy = h
    tx, ty = t
    if tx + 1 < hx:
        tx += 1
        if ty < hy:
            ty += 1
        elif ty > hy:
            ty -= 1
    elif tx - 1 > hx:
        tx -= 1
        if ty < hy:
            ty += 1
        elif ty > hy:
            ty -= 1

    elif ty + 1 < hy:
        ty += 1
        if tx < hx:
            tx += 1
        elif tx > hx:
            tx -= 1
    elif ty - 1 > hy:
        ty -= 1
        if tx < hx:
            tx += 1
        elif tx > hx:
            tx -= 1

    return (tx, ty)


for task in tasks:
    m, c = task.split()
    c = int(c)
    move_h(c, m)
print(len(ans))
