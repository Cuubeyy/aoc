task = open(0).read().splitlines()

list_one = []
list_two = []

for line in task:
    a, b = line.split()
    list_one.append(a)
    list_two.append(b)

list_one.sort()
list_two.sort()

# part 1
t1 = 0
for l, r in zip(list_one, list_two):
    t1 += abs(int(l) - int(r))
print(t1)

# part 2
t2 = 0
for l, r in zip(list_one, list_two):
    x = list_two.count(l)
    t2 += int(l) * x

print(t2)
