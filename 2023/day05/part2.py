from collections import defaultdict
from datetime import datetime

start = datetime.now()
task = open("input.txt").read().splitlines()
seeds = list(map(int, task.pop(0).split(": ")[1].split()))
seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
task.pop(0)
temp_seeds = seeds.copy()
changed = defaultdict(lambda: False)

for line_index, line in enumerate(task):
    seeds = [seed for seed in temp_seeds]
    if line == "":
        changed = defaultdict(lambda: False)
        continue
    elif "map" in line:
        continue
    mapped_start, source_start, source_length = list(map(int, line.split()))
    for seed_index, seed in enumerate(seeds):
        if changed[seed_index]:
            continue
        seed_start, seed_length = seed
        if source_start <= seed_start < source_start + source_length:
            if seed_start + seed_length <= source_start + source_length:
                seed_1 = (mapped_start + abs(seed_start - source_start), seed_length)
                temp_seeds[seed_index] = seed_1
                changed[seed_index] = True
            else:
                seed_1 = (mapped_start + abs(source_start - seed_start),
                          seed_length - abs(seed_start + seed_length - source_start - source_length))
                seed_2 = (seed_start + seed_length - abs(seed_start + seed_length - source_start - source_length),
                          abs(seed_start + seed_length - source_start - source_length))
                temp_seeds[seed_index] = seed_1
                temp_seeds.append(seed_2)
                changed[seed_index] = True
        elif source_start < seed_start + seed_length - 1 <= source_start + source_length - 1:
            x, y = (source_start + source_length - 1, seed_start + seed_length - 1)
            seed_2 = (seed_start, abs(source_start - seed_start))
            seed_1 = (mapped_start, seed_length - abs(source_start - seed_start))
            temp_seeds[seed_index] = seed_1
            temp_seeds.append(seed_2)
            changed[seed_index] = True

        elif seed_start < source_start + source_length-1 < seed_start + seed_length:
            seed_2 = (seed_start, abs(source_start - seed_start))
            seed_1 = (mapped_start,
                      seed_length - abs(source_start - seed_start) -
                      abs((seed_start + seed_length) - (source_start + source_length)))
            seed_3 = (seed_start + seed_length - abs(seed_start + seed_length - source_start - source_length),
                      abs((seed_start + seed_length) - (source_start + source_length)))

            temp_seeds[seed_index] = seed_1
            temp_seeds.append(seed_2)
            temp_seeds.append(seed_3)
            changed[seed_index] = True
print(sorted(temp_seeds, key=lambda x: x[0])[0][0])
print(datetime.now() - start)
