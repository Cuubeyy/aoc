import sys

sys.setrecursionlimit(10**4)


class File:
    def __init__(self, filename, filesize):
        self.name = filename
        self.size = filesize

    def get_size(self):
        return self.size

    def __str__(self):
        return "Name: " + self.name + " size: " + str(self.size)


class Directory:
    def __init__(self, dname):
        self.name = str(dname)
        self.files = []
        self.size = 0

    def add_file(self, add_file):
        self.files.append(add_file)

    def get_size(self):
        self.size = 0
        for f in self.files:
            s = f.get_size()
            self.size += s
        return self.size

    def __str__(self):
        return "Name: " + self.name + " Size: " + str(self.size)


task = open("input.txt").read().split("$ ")
task1 = []
for t in task:
    task1.append(t.splitlines())

main = Directory("main")
di = []
lastD = [main]
cur = ""

for block in task1:
    if not block:
        continue
    command = block[0]

    if command.startswith("cd "):
        if ".." in command:
            c = cur.split(">>>")
            c.pop(-1)
            cur = ">>>".join(c)
            continue
        cur += ">>>" + command[3:]
        directory = Directory(cur)
        di.append([directory, cur])

    if command == "ls":
        for line in block[1:]:
            if line.startswith("dir "):
                name = line[4:]
                for d in di:
                    if d[1] == cur:
                        direc = Directory(cur + ">>>" + name)
                        if not direc.name in (f.name for f in d[0].files):
                            di.append([direc, direc.name])
                            d[0].add_file(direc)
                continue
            size, name = line.split()
            file = File(cur + ">>>" + name, int(size))
            for d in di:
                if d[0].name == cur:
                    d[0].add_file(file)
                    break

ans = []
for d in di:
    s = d[0].get_size()
    if s > 0:
        ans.append(s)

ans = 70000000 - max(ans)
p = []
for d in di:
    s = d[0].get_size()
    if s > 0:
        if ans + s >= 30000000:
            p.append(s)
print(min(p))
