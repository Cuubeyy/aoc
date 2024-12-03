import re

ans = 0
ans2 = 0

task = open("03.in").read()
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don't\(\))", task)
do = True
for m in matches:
    if m[2] == r"do()":
        do = True
    elif m[2] == r"don't()":
        do = False
    else:
        a, b = list(map(int, m[:2]))
        ans += a * b
        ans2 += a * b if do else 0

print(ans)
print(ans2)
