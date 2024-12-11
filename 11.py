from aoctools.Input import Input
from functools import cache

@cache
def stones_left(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return stones_left(1, steps - 1)
    if l % 2 == 0:
        a = int(str(stone)[:len(str(stone)) // 2])
        b = int(str(stone)[len(str(stone)) // 2:])
        return stones_left(a, steps - 1) + stones_left(b, steps - 1)
    return stones_left(stone * 2024, steps - 1)


def rules(stone):
    if stone == 0:
        stone = 1
        return stone
    if len(str(stone)) % 2 == 0:
        a = int(str(stone)[:len(str(stone)) // 2])
        b = int(str(stone)[len(str(stone)) // 2:])
        return a, b
    stone *= 2024
    return stone


task = Input().get_input()
stones = list(map(int, task.split()))
ans = 0
for stone in stones:
    ans += stones_left(stone, 75)

for i in range(25):
    new_stones = []
    for j in range(len(stones)):
        x = rules(stones[j])
        try:
            for xx in x:
                new_stones.append(xx)
        except:
            new_stones.append(x)
    stones = new_stones

print(len(stones))
print(ans)
