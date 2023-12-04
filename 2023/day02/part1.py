task = open("input.txt").read().splitlines()
ans = 0

for line in task:
    split = line.split(": ")
    game_id = int(split[0].replace("Game ", ""))
    valid = True
    split = split[1].split(";")

    for sed in split:
        dic = {}
        cubes = sed.split(", ")

        for cube in cubes:
            cube = cube.split()
            dic[cube[1]] = int(cube[0])

        for k in dic:
            if k == "blue" and dic[k] > 14:
                valid = False
            if k == "green" and dic[k] > 13:
                valid = False
            if k == "red" and dic[k] > 12:
                valid = False

    print(valid)
    ans += game_id if valid else 0

print(ans)
