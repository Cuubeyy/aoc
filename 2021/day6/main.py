cmds = open("testinput.txt").read().split(",")

fischis = []

for cmd in cmds:
    fischis.append(int(cmd))

print(fischis, len(fischis))

for day in range(256):
    for fisch in range(len(fischis)):
        if fischis[fisch] == 0:
            fischis.append(8)
            fischis[fisch] = 7
        fischis[fisch] -= 1
    print("After " + str(day + 1) + " days: ", fischis, len(fischis))
print("After " + str(day) + " days: ", len(fischis))

# part 1: 394994