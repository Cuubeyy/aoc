task = open("input.txt").read().splitlines()

ans = 0

for i in task:
    ans += int(i)

print(ans)
