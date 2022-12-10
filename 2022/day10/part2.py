task = open("input.txt").read().splitlines()

x = 1
cycle = 0

grid = [["."] * 40, ["."] * 40, ["."] * 40, ["."] * 40, ["."] * 40, ["."] * 40]


def print_grid():
    for g in grid:
        print("".join(g))
    print("\n")


def make_grind(y, c, g):
    row = int((c-1) / 40)
    column = (c-1) % 40
    if column+1 in [y+i for i in range(3)]:
        grid[row][column] = "\u2588"
    else:
        grid[row][column] = " "
    print_grid()


for i in task:
    if i == "noop":
        cycle += 1
        make_grind(x, cycle, grid)
    elif i.split()[0] == "addx":
        for j in range(2):
            cycle += 1
            make_grind(x, cycle, grid)
        x += int(i.split()[1])
print_grid()
