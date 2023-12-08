task = open("input.txt").read().splitlines()
ans = 0
winning = []

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
    elif max(amounts) == 3:
        if min(amounts) == 2:
            score = 3
        else:
            score = 4
    elif max(amounts) == 2:
        if amounts.pop(-1):
            if min(amounts) == 2:
                score = 5
            else:
                score = 6
    elif max(amounts) == 1:
        score = 7
    winning.append([score, hand, amounts, bit])


def get_highest_card(cards_):
    dictionary = {"A": 99, "K": 90, "Q": 89, "J": 80, "T": 79, "9": 70, "8": 69, "7": 60, "6": 50,
           "5": 40, "4": 30, "3": 20, "2": 10}
    sorted_cards = []
    for card_ in cards_:
        amount_ = ""
        for c in card_[1]:
            amount_ += str(dictionary[c])
        card_.append(int(amount_))
        sorted_cards.append(card_)
    return sorted_cards


cards = list(sorted(get_highest_card(sorted(winning, key=lambda x: (-x[0], x[1]))), key=lambda x: (-x[0], int(x[-1]))))
rank, ans = 0, 0
for i, w in enumerate(cards):
    rank += 1
    ans += w[3] * rank
print(ans)
