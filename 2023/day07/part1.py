import operator
import os
from collections import defaultdict

from aocd import get_data

task = open("input.txt").read().splitlines()
ans = 0
winning = {}
winning_2 = []

for card_index, line in enumerate(task):
    hand, bit = line.split()
    bit = int(bit)
    value = set()
    for card in hand:
        amount = hand.count(card)
        value.add((card, amount))

    value = sorted(value, key=lambda x: x[1], reverse=True)
    amounts = []
    for amount in value:
        amounts.append(amount[1])
    if amounts == [5]:
        winning_2.append((1, hand, amounts, bit))
    elif amounts == [4, 1]:
        winning_2.append((2, hand, amounts, bit))
    elif amounts == [3, 2]:
        winning_2.append((3, hand, amounts, bit))
    elif amounts == [3, 1, 1]:
        winning_2.append((4, hand, amounts, bit))
    elif amounts == [2, 2, 1]:
        winning_2.append((5, hand, amounts, bit))
    elif amounts == [2, 1, 1, 1]:
        winning_2.append((6, hand, amounts, bit))
    elif amounts == [1, 1, 1, 1, 1]:
        winning_2.append((7, hand, amounts, bit))


def get_highest_card(cards_):
    c_h = []
    dic = {"A": 990, "K": 900, "Q": 890, "J": 800, "T": 790, "9": 700, "8": 690, "7": 600, "6": 500,
           "5": 400, "4": 300, "3": 200, "2": 100}
    for card in cards_:
        amount = ""
        for i, c in enumerate(card[1]):
            amount += str(dic[c])
        t = [cd for cd in card]
        t.append(amount)
        c_h.append(t)
    return c_h


cards = sorted(winning_2, key=lambda x: (-x[0], x[1]))
cards = get_highest_card(cards)
cards = sorted(cards, key=lambda x: (-x[0], int(x[-1])))
print(cards)
rank = 1
ans = 0
for i, w in enumerate(cards):
    ans += w[3] * rank
    print(w[3], rank, w[1])
    rank += 1
print(ans)
