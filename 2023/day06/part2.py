task = open("input.txt").read().splitlines()
time = int("".join(task[0].split()[1:]))
distance = int("".join(task[1].split()[1:]))
ans, speed, win = 1, 0, 0

for i in range(time):
    missing_time = time - i
    if speed * missing_time > distance:
        win += 1
    speed += 1
ans *= win
print(ans)
