class Node:
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.followers = []
        self.appendet = []

    def find_way(self, beforeP, path):
        print(self.id, chr(self.id), self.position)
        path.append(self.position)
        for f in self.followers:
            if f.position != beforeP:
                return f.find_way(self.position, path)
            return path

    def __str__(self):
        return "ID: " + str(self.id) + " position: " + str(self.position) + " followers: " + str(self.followers)

    def add_follower(self, follower):
        if self.position == (6, 2):
            pass
        if follower.game_id == self.id or follower.game_id == self.id + 1:
            self.followers.append(follower)
            self.appendet.append(follower.position)


task = open("test.txt").read().splitlines()
nodes = []
grid = []
for i in range(len(task)):
    t = task[i]
    temp = []
    for k in t:
        k = ord(k)
        if k == ord("S"):
            ax, ay = (t.index("S"), i)
            k = ord("a")-1
        elif k == ord("E"):
            bx, by = (t.index("E"), i)
            k = ord("z")+1
        temp.append(k)
    grid.append(temp)

for row_i in range(len(grid)):
    row = grid[row_i]
    for position_i in range(len(row)):
        position = row[position_i]
        node = Node(position, (position_i, row_i))
        nodes.append([node, (position_i, row_i)])

for node, position in nodes:
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if position[0] + direction[0] >= 0 and position[1] + direction[1] >= 0:
            next_node = (node.position[0] + direction[0], node.position[1] + direction[1])
            for n in nodes:
                if n[1] == next_node:
                    node.add_follower(n[0])
                    break

startnode = None
for n in nodes:
    if n[1] == (ax, ay):
        startnode = n[0]
        break
path = startnode.find_way((-1, 0), [])
print(path, len(path)+1)

grid2 = []
for g in grid:
    g = list(map(chr, g))
    grid2.append(g)
for p in path:
    grid2[p[1]][p[0]] = str(path.index(p))
for g in grid2:
    print(g)
