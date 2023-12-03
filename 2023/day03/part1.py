task = open("test.txt").read().splitlines()
ans = 0


def is_valid(matrix, x, y, length):
    for i in range(-1, 2):
        if y + i < 0:
            continue
        for j in range(-length, 2):
            if x + j < 0:
                continue
            try:
                b = matrix[y + i][x + j]
                if not b.isdigit():
                    if not b == ".":
                        return True
            except:
                pass
    return False


for index, line in enumerate(task):
    number = ""
    for line_index, x in enumerate(line):
        if x.isdigit():
            number += x
            if line_index == len(line) - 1 or not line[line_index + 1].isdigit():
                if is_valid(task, line_index, index, len(number)):
                    ans += int(number)
                number = ""

print(ans)
