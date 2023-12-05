from datetime import datetime

start = datetime.now()
task = open("input.txt").read().splitlines()
ans = 10e10

seeds = list(map(int, task.pop(0).split(": ")[1].split()))
task.pop(0)
temp_seeds = [seed for seed in seeds]

for line_index, line in enumerate(task):
    possible = []
    if line == "":
        seeds = [seed for seed in temp_seeds]
        continue
    elif "map" in line:
        continue
    destination, range_start, source_range = line.split()
    for seed_index, seed in enumerate(seeds):
        if int(range_start) <= seed <= int(range_start) + int(source_range):
            temp_seeds[seed_index] = int(destination) + (seed - int(range_start))

seeds = temp_seeds
print(min(seeds))
print(datetime.now() - start)
