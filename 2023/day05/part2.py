from collections import defaultdict

task = open("test.txt").read().splitlines()
ans = 10e10

seeds = list(map(int, task.pop(0).split(": ")[1].split()))
seeds = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
task.pop(0)
temp_seeds = seeds.copy()
did = defaultdict(lambda: False)

for line_index, line in enumerate(task):
    if line == "":
        seeds = [seed for seed in temp_seeds]
        print("ending:", seeds)
        continue
    elif "map" in line:
        did = defaultdict(lambda: False)
        print(line.split()[0].split("-")[2])
        print("beginning:", seeds)
        continue
    mapped_start, source_start, source_length = list(map(int, line.split()))
    for seed_index, seed in enumerate(seeds):
        if did[seed_index]:
            continue
        seed_start, seed_length = seed
        if source_start <= seed_start <= source_start + source_length:
            if seed_start + seed_length <= source_start + source_length:
                temp_seeds[seed_index] = (mapped_start, seed_length)
                did[seed_index] = True
            else:
                seed_1 = (mapped_start, source_length - abs(source_start - seed_start))
                seed_2 = (seed_start + source_length - abs(source_start - seed_start), abs(source_start + source_length - seed_start - seed_length))
                temp_seeds[seed_index] = seed_1
                temp_seeds.append(seed_2)
                did[seed_index] = True
                did[len(temp_seeds)] = True

print(temp_seeds)