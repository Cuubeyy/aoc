task = open("input.txt").read().splitlines()

most = []
before = []

for i in task:
    if i == '':
        most.append(sum(before))
        before = []
        continue

    before.append(int(i))

print(sum(sorted(most)[-3:]))