from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans = 0

# line by line input
task = Input().get_input()

room, moves = task.split("\n\n")
room = [list(x) for x in room.splitlines()]
walls = set()
boxes = []
empty = set()
position = (0, 0)
size = (len(room), len(room[0]) * 2)


def printg(p=True):
    grid = [list("." for x in range(size[1])) for _ in range(size[0])]
    for w in walls:
        grid[w[0]][w[1]] = "#"
    for b in boxes:
        grid[b[0]][b[1]] = "["
    grid[position[0]][position[1]] = "@"
    if p:
        for g in grid:
            g = "".join(g)
            g = g.replace("[.", "[]")
            print(g)
        print("-----------")
    return grid


b_map = {}

for col in range(len(room)):
    for row in range(len(room[0])):
        ch = room[col][row]
        if ch == "#":
            walls.add((col, row * 2))
            walls.add((col, row * 2 + 1))
        elif ch == "@":
            position = (col, row * 2)
        elif ch == "O":
            boxes.append((col, row * 2))
room = printg()

move_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

for move in moves:
    def can_move(direction, pcol, prow, to_move):
        if (pcol,prow) in to_move:
            return True, to_move
        ch = room[pcol][prow]
        if ch == ".":
            if room[pcol][prow-1] == "[":
                t1, a1 = can_move(direction, pcol, prow - 1, to_move)
                t2, a2 = can_move(direction, pcol + direction[0], prow + direction[1], to_move)
                if t1 and t2:
                    a1.update(a2)
                    return True, a1
                else:
                    return False, []
            return True, to_move
        elif ch == "#":
            return False, []
        elif ch == "[":
            to_move.add((pcol, prow))
            t1, a1 = can_move(direction, pcol+direction[0], prow+direction[1], to_move)
            t2, a2 = can_move(direction, pcol, prow+1, to_move)
            if t1 and t2:
                a1.update(a2)
                return True, a1
            return False, []
        elif ch == "@":
            to_move.add((pcol, prow))
            return can_move(direction, pcol + direction[0], prow + direction[1], to_move)
        return False, []


    def move_c(direction, blocks_to_move):
        global position
        global boxes
        new_blocks = boxes.copy()
        for box in blocks_to_move:
            if box == position:
                new_pos = (position[0] + direction[0], position[1] + direction[1])
                continue
            new_blocks.remove(box)
            new_blocks.append((box[0]+direction[0], box[1]+direction[1]))
        boxes = new_blocks
        position = new_pos

    cmove, to_move = can_move(move_map[move], position[0], position[1], set())
    if cmove:
        move_c(move_map[move], sorted(list(to_move)))
    room = printg(False)
for x in boxes:
    ans += x[0] * 100 + x[1]
print(ans)
