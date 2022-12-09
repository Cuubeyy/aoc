task = open("input.txt").read().splitlines()
ans1 = -1
ans2 = -1
for i in task:
    a = []
    for j in i:
        if i.count(j) == 2 and j not in a:
            ans1 += 1
        elif i.count(j) == 3 and j not in a:
            ans2 += 1
        a.append(j)
print(ans1, ans2, ans1*ans2)