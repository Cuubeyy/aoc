task = open("input.txt").read().splitlines()
ans = 0

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, 1: 1,
               2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}


def getFirstNumber(new_line):
    global numbers
    summe = 0
    for i in range(len(new_line)):
        temp_line = new_line[i:]
        for number in numbers:
            if temp_line.startswith(str(number)):
                return numbers[number]


def getSecondNumber(new_line):
    global numbers
    for i in range(len(new_line), -1, -1):
        temp_line = new_line[:i]
        for number in numbers:
            if temp_line.endswith(str(number)):
                return numbers[number]


for line in task:
    ans += getFirstNumber(line) * 10 + getSecondNumber(line)

print(ans)
