task = open("03.in").read().splitlines()

ans = 0
ans1 = 0
do = True

for line in task:
    while len(line) > 0:
        if line.startswith("do()"):
            do = True
        if line.startswith("don't()"):
            do = False
        if not line.startswith("mul("):
            line = line[1:]
            continue
        x = line[:12]
        if ")" not in x:
            line = line[1:]
            continue

        x = x.split(")")[0].split("(")[1]
        try:
            a, b = x.split(",")
        except:
            line = line[1:]
            continue
        if " " in a or " " in b:
            line = line[1:]
            continue
        try:
            a, b = int(a), int(b)
        except:
            line = line[1:]
            continue
        ans += a*b
        ans1 += a*b if do else 0
        line = line[1:]

print(ans)
print(ans1)
