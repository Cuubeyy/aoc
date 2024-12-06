from aoctools.TextGrid import TextGrid
from aoctools.Input import Input


def solve(matrix):
    position = start.copy()[0]
    coords = set()
    c = 0
    direction = directions[c]
    dirc = set()
    coords.add(position)
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    max_iterations = (rows + 1) * (cols + 1) * 10

    for _ in range(max_iterations):
        state = (position[0], position[1], direction[0], direction[1])
        if state in dirc:
            return True
        dirc.add(state)

        if not (0 <= position[0] <= cols and 0 <= position[1] <= rows):
            return coords

        next_pos = (position[0] + direction[0], position[1] + direction[1])

        if next_pos in turns:
            c = (c + 1) % 4
            direction = directions[c]
        else:
            position = next_pos

        coords.add(position)
    return coords


ans = 0
task = Input().get_input().splitlines()

grid = TextGrid(task)
turns = set(grid.find_pattern_in_grid("#"))
start = grid.find_pattern_in_grid("^")

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

co = solve(task)
print(len(co)-1)
for i in range(len(task)):
    for j in range(len(task[0])):
        if j == 3 and i == 6:
            pass
        if task[i][j] == "#" or task[i][j] == "^":
            continue
        if (i, j) not in co:
            continue
        nt = task.copy()
        nt[i] = list(nt[i])
        nt[i][j] = "#"
        nt[i] = "".join(nt[i])
        turns.add((i, j))
        loop = solve(nt)
        turns.remove((i, j))
        if loop == True:
            ans += 1
print(ans)
