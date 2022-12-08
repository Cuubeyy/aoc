data = open("input.txt").read().splitlines()

data = list(map(int, data))

ans = [0]
x = 0

for i in data:
    if i > ans[-1]:
        x += 1
    ans.append(i)
print(x-1)