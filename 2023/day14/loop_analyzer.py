import ast

file = open("output1.txt").read().splitlines()

beginning = file.index(file[-1])

loop_size = abs(2 + beginning - len(file))
print(loop_size)
s = set()
for f in file:

    ans = 0
    rocks = ast.literal_eval(f)

    for rock in rocks:
        ans += len(file) - int(rock[1])

    print(ans)
