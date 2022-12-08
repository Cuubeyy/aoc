data = open("input.txt").read().splitlines()

data = list(map(int, data))

ans = [0]
x = 0

for i in data:
    print(sum(ans[-3:]))
    if sum(ans[-2:]) + i > sum(ans[-3:]):
        x += 1
    ans.append(i)
print(x-1)