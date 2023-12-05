from collections import defaultdict

task = open("input.txt").read().splitlines()
ans = 10e10

seeds = list(map(int, task.pop(0).split(": ")[1].split()))
seeds = [range(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
seeds = [item for sublist in seeds for item in sublist]
task.pop(0)
temp_seeds = seeds.copy()
did = defaultdict(bool)


for line_index, line in enumerate(task):
    if line == "":
        seeds = [seed for seed in temp_seeds]
        print("ending:", seeds)
        continue
    elif "map" in line:
        did = defaultdict(bool)
        print(line.split()[0].split("-")[2])
        print("beginning:", seeds)
        continue
    destination, range_start, source_range = line.split()
    for seed_index, seed in enumerate(seeds):
        if not did[seed_index]:
            if int(range_start) <= seed <= int(range_start) + int(source_range):
                temp_seeds[seed_index] = int(destination) + (seed - int(range_start))
                did[seed_index] = True

print(min(temp_seeds))