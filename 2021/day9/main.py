cmds = open("testinput.txt").read().splitlines()

risklevel = 0

def get_nearest(line, cmdID, linelen):
    if line == 2 and line != linelen:
        up = int(cmds[line - 1][cmdID])
        left = int(cmds[line][cmdID - 1])
        right = int(cmds[line - 1][cmdID + 1])
        down = int(cmds[line + 1][cmdID])
        return up, left, right, down


for line in cmds:
    for cmdID in range(len(line)):
        up, left, right, down = get_nearest(int(line), int(cmdID), len(line))
        print(up, left, right, down)