import os
from aocd import get_data

task = open("input.txt").read().splitlines()
ans = 0

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "eight": 8, "nine": 9, 1: 1, 2: 2, 3: 3,
           4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
lines = []

for line in task:
    temp = []
    for n in numbers:
        if line.find(str(n)) != -1:
            y = [i for i in range(len(line)) if line.startswith(str(n), i)]
            print(y)
            for yy in y:
                temp.append((numbers[n], yy))

    if temp:
        temp.sort(key=lambda x: x[1])
        print(temp)
        lines.append(temp)

for line in lines:
    z = "".join([str(line[0][0]), str(line[-1][0])])
    ans += int(z)
print(ans)

# 53502 FALSE
# 53450 FALSE
