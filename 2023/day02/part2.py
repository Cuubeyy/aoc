task = open("input.txt").read().splitlines()
ans = 0

red_max, green_max, blue_max = 12, 13, 14

for line in task:
    highest_green, highest_blue, highest_red = 0, 0, 0

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
                if dic[k] > highest_blue:
                    highest_blue = dic[k]
            if k == "red":
                if dic[k] > highest_red:
                    highest_red = dic[k]
            if k == "green":
                if dic[k] > highest_green:
                    highest_green = dic[k]

    print(highest_red, highest_green, highest_blue)
    ans += (highest_red * highest_green * highest_blue)

print(ans)
