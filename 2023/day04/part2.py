from collections import defaultdict

task = open("input.txt").read().splitlines()
ans = 0

cards = defaultdict(lambda: 1)

for card_number, line in enumerate(task):
    temp_win = 0
    winning, numbers = line.split(": ")[1].split(" | ")

    winning = winning.split()
    numbers = numbers.split()
    for n in numbers:
        if n in winning:
            temp_win += 1

    for l in range(cards[str(card_number)]):
        for i in range(temp_win):
            cards[str(card_number + 1 + i)] += 1
            
for c in cards:
    ans += cards[c]
print(ans)

# 1070 FALSE
