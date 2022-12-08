task = open("input.txt").read().splitlines()
ans = 0

win = 6
even = 3
loss = 0

enemy_map = {"A":0, "B":1, "C":2}
game_map = {"X":0, "Y":1, "Z":2}

rps_table = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

for i in task:
    i = i.split()
    enemy = i[0]
    you = i[1]

    you = game_map[you]
    enemy = enemy_map[enemy]

    temp = 0
    tableW = rps_table[you][enemy]

    if tableW == 1:
        temp = win
    elif tableW == 0:
        temp = even
    elif tableW == -1:
        temp = loss

    ans += temp
    if you == 0:
        ans += 1
    elif you == 1:
        ans += 2
    elif you == 2:
        ans += 3


print(ans)