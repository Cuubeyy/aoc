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


def get_highest_card(cards_):
    c_h = []
    dic = {"A": 99, "K": 90, "Q": 89, "J": "00", "T": 79, "9": 70, "8": 69, "7": 60, "6": 50,
           "5": 40, "4": 30, "3": 20, "2": 10}
    for card_stats in cards_:
        count = ""
        for c in card_stats[1]:
            count += str(dic[c])
        t = [cd for cd in card_stats]
        t.append(int(count))
        c_h.append(t)
    return c_h


cards = sorted(get_highest_card(sorted(winning_2, key=lambda x: (-x[0], x[1]))), key=lambda x: (-x[0], x[-1]))
rank, ans = 0, 0
for i, w in enumerate(cards):
    rank += 1
    ans += w[3] * rank
print(ans)
