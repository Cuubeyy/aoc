task = open("input.txt").read().splitlines()

x = 1
cycle = 0
ans = 0


def print_ans():
    global ans, x, cycle
    print(x, cycle)
    if (20 + cycle) % 40 == 0 or cycle == 20:
        ans += cycle * x
        print(cycle * x)


for i in task:
    if i == "noop":
        cycle += 1
        print_ans()
    elif i.split()[0] == "addx":
        for j in range(2):
            cycle += 1
            print_ans()
        x += int(i.split()[1])
print(x, ans)
