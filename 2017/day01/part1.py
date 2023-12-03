with open("input.txt", "r") as file:
    task = file.read().strip()
ans = 0
length = len(task)
for index, x in enumerate(task):
    next_index = (index + 1) % length
    if x == task[next_index]:
        ans += int(x)
print(ans)
