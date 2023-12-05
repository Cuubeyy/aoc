task = open("test.txt").read().splitlines()
ans = 10e10

seeds = list(map(int, task.pop(0).split(": ")[1].split()))
seeds = [range(seeds[0], seeds[0]+seeds[1]), range(seeds[2], seeds[2]+seeds[3])]
seeds = [[item] for sublist in seeds for item in sublist]
task.pop(0)
temp_seeds = seeds.copy()
maps = []
temp_maps = []
counter = 0
for line_index, line in enumerate(task):
    possible = []
    if line == "":
        maps.append(temp_maps)
        seeds = temp_seeds.copy()
        print("ending:", seeds)
        continue
    elif "map" in line:
        print(line.split()[0].split("-")[2])
        print("beginning:", seeds)
        temp_maps = []
        continue
    counter += 1
    destination, range_start, source_range = line.split()
    for seed_index, seed in enumerate(seeds):
        print(counter, len(seed))
        if len(seed) != counter:
            if int(range_start) <= seed[-1] <= int(range_start) + int(source_range):
                temp_seeds[seed_index].append(int(destination) + (seed[-1] - int(range_start)))


seeds = temp_seeds.copy()
seeds.sort(key=lambda x: x[-1])
print(seeds[0][-1])
