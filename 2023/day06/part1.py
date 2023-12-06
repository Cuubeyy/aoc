task = open("input.txt").read().splitlines()
times = list(map(int, task[0].split()[1:]))
distances = list(map(int, task[1].split()[1:]))
ans = 1

for time_index, time in enumerate(times):
    distance = distances[time_index]
    speed, win = 0, 0
    for i in range(time):
        missing_time = time - i
        if speed * missing_time > distance:
            win += 1
        speed += 1
    ans *= win
print(ans)
