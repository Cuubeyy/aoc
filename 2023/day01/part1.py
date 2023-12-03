task = open("input.txt").read().splitlines()
ans = 0
for line in task:
    y = ([str(x) for x in line if x.isdigit()])
    ans += int("".join([y[0], y[-1]]))
print(ans)
