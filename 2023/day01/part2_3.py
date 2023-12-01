task = open("test.txt").read().splitlines()
ans = 0

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

lines = []
for line in task:
    line2 = line
    for number in numbers:
        line2 = line2.replace(number, str(numbers[number]))

    temp = []
    for x in line:
        if x.isdigit():
            temp.append(x)
    lines.append(temp)

for line in task:
    summe = 0
    for i in range(len(lines)):
        new_line = line[i:]
        for number in numbers:
            if line.startswith(str(number)):
                summe += numbers[number]

print(ans)
