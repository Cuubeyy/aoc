commands = open("Input.txt").read().splitlines()

ans = 0


def draw_line(x1, y1, x2, y2):
    line = []
    if x1 != x2 and y1 == y2:
        if x1 > x2:
            for i in range((x1 - x2) + 1):
                line.append([x1 - i, y1])
        else:
            for i in range((x2 - x1) + 1):
                line.append([x1 + i, y1])
    elif y1 != y2 and x1 == x2:
        if y1 > y2:
            for i in range((y1 - y2) + 1):
                line.append([x1, y1 - i])
        else:
            for i in range((y2 - y1) + 1):
                line.append([x1, y1 + i])
    else:
        if x1 == y2 and x2 == y1:
            if y1 > y2:
                for i in range((y1 - y2) + 1):
                    line.append([x1 + i, y1 - i])
            else:
                for i in range((y2 - y1) + 1):
                    line.append([x1 - i, y1 + i])
        else:
            if y1 > y2:
                for i in range((y1 - y2) + 1):
                    line.append([x1 - i, y1 - i])
            else:
                for i in range((y2 - y1) + 1):
                    line.append([x1 + i, y1 + i])
    return line


lines = []
for command in commands:
    cmd = command.split(" -> ")
    for i in range(len(cmd)):
        if i == 0:
            x1, y1 = cmd[i].split(",")
        else:
            x2, y2 = cmd[i].split(",")

    line = draw_line(int(x1), int(y1), int(x2), int(y2))
    for l in line:
        lines.append(l)

elements = []
for elm in list(lines):
    count = lines.count(elm)
    if count > 1 and elm not in elements:
        elements.append(elm)
        ans += 1
        print(ans)

# 17586 too low
# 76559 too high