input = open("input.txt").read().splitlines()

times = 0


for line in range(len(input)):
    last_times = int(input[line-3]) + int(input[line-1]) + int(input[line-2])
    now_time = int(input[line]) + int(input[line-1]) + int(input[line-2])
    if now_time > last_times:
        times+=1
    print(times)