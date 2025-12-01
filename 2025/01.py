from aoctools.Input import Input


ans = 0
ans2 = 0
start = 50

task = Input().get_input().splitlines()
for line in task:
    indicator = True if line[0] == "L" else False
    num = int(line[1:])
    for i in range(int(line[1:])):
        if indicator:
            start = (start - 1) % 100
        else:
            start = (start + 1) % 100
        if start == 0:
            ans += 1
    if start == 0:
        ans2 += 1
print(ans2, ans)
