input = open("input.txt").read().splitlines()

aim = 0
high = 0
strecke = 0

for lines in input:
    line = lines.split(" ")
    if line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    elif line[0] == "forward":
        strecke += int(line[1])
        high += aim * int(line[1])
print(high * strecke)