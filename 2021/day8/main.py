cmds = open("input.txt").read().splitlines()
splittet = []

up = ""
leftup = ""
rightup = ""
middle = ""
leftdown = ""
rightdown = ""
down = ""

for cmd in cmds:
    splittet.append(cmd.split(" | "))

for parts in cmds:
    for part in parts:
