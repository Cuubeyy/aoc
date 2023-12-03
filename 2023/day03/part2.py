from collections import defaultdict

task = open("input.txt").read().splitlines()
ans = 0
stars = defaultdict(list)


def is_valid(matrix, x, y, lenth, num):
    for i in range(-1, 2):
        if y + i < 0:
            continue
        for j in range(-lenth, 2):
            if x + j < 0:
                continue
            try:
                b = matrix[y + i][x + j]
                if b == "*":
                    stars[(x+j, y+i)].append(int(num))
                    return True
            except:
                pass
    return False


for index, line in enumerate(task):
    number = ""
    for line_index, x in enumerate(line):
        if x.isdigit():
            if line_index == len(line) - 1 or not line[line_index + 1].isdigit():
                number += x
                is_valid(task, line_index, index, len(number), number)
                number = ""
            else:
                number += x

for star in stars:
    if len(stars[star]) == 2:
        ans += stars[star][0] * stars[star][1]
print(ans)
