task = open(0).read().splitlines()
ans = 0
ans2 = 0

def correct(nums):
    for i, n in enumerate(nums):
        if i == len(nums) - 1:
            return True
        if not 0 < nums[i+1] - n < 4:
            return False

for line in task:
    temp = list(map(int, line.split()))
    if temp[0] > temp[-1]:
        temp = temp[::-1]
    line2 = temp.copy()

    #part1
    if correct(line2):
        ans += 1

    #part2
    for i in range(len(line2)):
        l2 = line2.copy()
        l2.pop(i)
        if correct(l2):
            ans2 += 1
            break

print(ans)
print(ans2)
