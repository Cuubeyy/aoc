from datetime import datetime
import os
import math
from get_input import GetInput

start = datetime.now()


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        session = os.environ.get("AOC_SESSION")
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt").read()
    else:
        return open("test.txt").read()


class Broadcast:
    pass


def parse_data():
    data = get_input(True).splitlines()

    for l in data:
        name, targets = l.split(" -> ")
        targets = targets.split(", ")

        if name == "broadcaster":
            broadcaster = Broadcast(targets)

    return data


ans = 0
task = parse_data()
for line in task:
    if line == '':
        continue
    ans += int(line)

print(ans)
print(datetime.now() - start)
