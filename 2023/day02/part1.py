task = open("input.txt").read().splitlines()
ans = 0

red_max, green_max, blue_max = 12, 13, 14

for line in task:

    splitted = line.split(": ")
    id = int(splitted[0].replace("Game ", ""))
    valid = True
    splitted = splitted[1].split(";")

    for sed in splitted:
        dic = {}
        cubes = sed.split(", ")

        for cube in cubes:
            cube = cube.split()
            dic[cube[1]] = int(cube[0])

        for k in dic.keys():
            if k == "blue":
                if dic["blue"] > 14:
                    valid = False
            if k == "green":
                if dic["green"] > 13:
                    valid = False
            if k == "red":
                if dic["red"] > 12:
                    valid = False

    print(valid)
    ans += id if valid == True else 0

print(ans)
