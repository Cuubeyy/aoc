task = open(0).read().splitlines()
ans, ans2 = 0, 0


def correct(nums):
    for i, n in enumerate(nums):
        if i == len(nums) - 1:
            return True
        if not 0 < nums[i + 1] - n < 4:
            return False


for line in task:
    line = list(map(int, line.split()))
    if line[0] > line[-1]:
        line = line[::-1]

    #part1
    if correct(line):
        ans += 1

    #part2
    for i in range(len(line)):
        l2 = line.copy()
        l2.pop(i)
        if correct(l2):
            ans2 += 1
            break

print(ans)
print(ans2)
