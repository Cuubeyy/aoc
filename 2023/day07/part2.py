from collections import defaultdict

task = open("input.txt").read().splitlines()
winning_2 = []

for card_index, line in enumerate(task):
    hand, bit = line.split()
    bit = int(bit)
    value = set()
    jokers = hand.count("J")
    for card in hand:
        if card == "J":
            value.add((card, jokers))
        else:
            amount = hand.count(card) + jokers
            value.add((card, amount))

    value = sorted(value, key=lambda x: x[1], reverse=True)
    amounts = []
    for amount in value:
        amounts.append(amount[1])
    score = 0
    print(amounts)
    if max(amounts) == 5:
        score = 1
    elif max(amounts) == 4:
        score = 2
    elif max(amounts) == 3:
        amounts.pop(0)
        if max(amounts) - jokers == 2:
            score = 3
        else:
            score = 4
    elif max(amounts) == 2:
        amounts.pop(-1)
        if min(amounts) == 2 + jokers:
            score = 5
        else:
            score = 6
    else:
        score = 7
    winning_2.append((score, hand, amounts, bit))
    print(hand, score)


def get_highest_card(cards_):
    c_h = []
    dic = {"A": 990, "K": 900, "Q": 890, "J": "000", "T": 790, "9": 700, "8": 690, "7": 600, "6": 500,
           "5": 400, "4": 300, "3": 200, "2": 100}
    for card in cards_:
        amount = ""
        for c in card[1]:
            amount += str(dic[c])
        t = [cd for cd in card]
        t.append(int(amount))
        c_h.append(t)
    return c_h


cards = sorted(get_highest_card(sorted(winning_2, key=lambda x: (-x[0], x[1]))), key=lambda x: (-x[0], x[-1]))
print(cards)
rank, ans = 0, 0
for i, w in enumerate(cards):
    rank += 1
    ans += w[3] * rank
    # print(w[3], rank, w[1])
print(ans)

# 253295076 TOO LOW
