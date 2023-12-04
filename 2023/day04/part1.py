task = open("input.txt").read().splitlines()
ans = 0

for line in task:
    temp_win = 0
    winning, numbers = line.split(": ")[1].split(" | ")

    winning = winning.split()
    numbers = numbers.split()

    for n in numbers:
        if n in winning:
            if temp_win == 0:
                temp_win = 1
            else:
                temp_win *= 2
    ans += temp_win
print(ans)
