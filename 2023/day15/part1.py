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



ans = 0
task = get_input(True)
for group in task:
    count = 0
    for g in group:
        count += ord(g)
        count *= 17
        count = count % 256
    ans += count
print(ans)
print(datetime.now() - start)
