import copy
import math
from sys import set_int_max_str_digits

set_int_max_str_digits(10**9)

class Monkey:
    def __init__(self, id, items, operation, divisible, true, false):
        self.count = 0
        self.id = id
        self.items = items
        self.operation = operation
        self.test_operation = None
        self.divisible = divisible
        self.true = true
        self.false = false

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return "Monkey " + str(self.id) + ": " + " ".join(list(map(str, self.items)))


monkeys = []
monkeys2 = []

task = open("input.txt").read().split("\nMonkey ")
for line in task:
    temp = []
    temp2 = ""
    first, second = line.split("  Test: divisible by ")
    first = first.split("  Operation: ")
    for f in first:
        f = f.replace(":\n  Starting items: ", " ")
        f = f.replace("Monkey ", "")
        f = f.replace("new", "")
        f = f.replace("=", "")
        f = f.replace(",", "")
        f = f.split()
        temp.append(f)
    for s in second.split():
        s = s.replace("If", "")
        s = s.replace("throw", "")
        s = s.replace("to", "")
        s = s.replace("monkey", "")
        s = s.replace("false:", "")
        s = s.replace("true:", "")
        s = s.replace("\n", "")
        temp2 += str(s) + " "
    temp2 = temp2.split()
    temp.append(temp2)
    temp[0] = list(map(int, temp[0]))
    temp[2] = list(map(int, temp[2]))
    monkeys.append(Monkey(temp[0][0], temp[0][1:], temp[1], temp[2][0], temp[2][1], temp[2][2]))

x = 1
for m in monkeys:
    x *= m.divisible
    for i in m.items:
        x *= i
print(x)

for i in range(10000):
    for m in monkeys:
        removed = []
        for item in m.items:
            m.count += 1
            temp = []
            s = " "
            for o in m.operation:
                if o == "old":
                    o = item

                s += str(o)
            s = eval(s)%x
            if s % m.divisible == 0:
                monkeys[m.true].add_item(s)
            else:
                monkeys[m.false].add_item(s)
            removed.append(item)
        for r in removed:
            monkeys[m.id].items.remove(r)

ans = []
for m in monkeys:
    ans.append(m.count)
print(ans)
x, y = list(sorted(ans))[-2:]
print(x*y)

# 2635317092 too low
