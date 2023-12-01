task = open("input.txt").read().splitlines()
ans = 0

for i in task:
    if i == '':
        continue
    ans += int(i)

print(ans)