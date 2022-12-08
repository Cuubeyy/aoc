cmdsstr = open("input.txt").read().split(",")
cmds = list(map(int, cmdsstr))


def move(number, position):
    count = 0
    aim = 0
    for moves in range(abs(number - position)):
        count += 1 + aim
        aim += 1
    return count

answers = []

for steps in range(round(max(cmds)/2)):
    ans = 0
    for cmd in cmds:
        ans += move(cmd, steps)
    answers.append(ans)

print("Answer:", min(answers))


# 329389