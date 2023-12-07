task = open("input.txt").read().splitlines()
ans = 0
winning_2 = []

for card_index, line in enumerate(task):
    hand, bit = line.split()
    bit = int(bit)
    value = set((card, hand.count(card)) for card in hand)
    value = sorted(value, key=lambda x: x[1], reverse=True)
    amounts = [amount[1] for amount in value]
    score = 0

    if max(amounts) == [5]:
        score = 1
    elif max(amounts) == 4:
        score = 2
    elif amounts == [3, 2]:
        score = 3
    elif amounts == [3, 1, 1]:
        score = 4
    elif amounts == [2, 2, 1]:
        score = 5
    elif amounts == [2, 1, 1, 1]:
        score = 6
    elif amounts == [1, 1, 1, 1, 1]:
        score = 7
    winning_2.append((score, hand, amounts, bit))


def get_highest_card(cards_):
    c_h = []
    dic = {"A": 99, "K": 90, "Q": 89, "J": 80, "T": 79, "9": 70, "8": 69, "7": 60, "6": 50,
           "5": 40, "4": 30, "3": 20, "2": 10}
    for card_ in cards_:
        amount_ = ""
        for c in card_[1]:
            amount_ += str(dic[c])
        t = [cd for cd in card_]
        t.append(int(amount_))
        c_h.append(t)
    return c_h


cards = sorted(get_highest_card(sorted(winning_2, key=lambda x: (-x[0], x[1]))), key=lambda x: (-x[0], int(x[-1])))
rank, ans = 0, 0
for i, w in enumerate(cards):
    rank += 1
    ans += w[3] * rank
print(ans)
