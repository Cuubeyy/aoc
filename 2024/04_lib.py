from aoctools.TextGrid import TextGrid
from aoctools.Input import Input

# grid_input
task = Input().get_input().splitlines()
grid = TextGrid(task)
ans1 = grid.find_string_in_grid("XMAS")
print(len(ans1))

patterns = ["""M.S
.A.
M.S""",
"""M.M
.A.
S.S""",
"""S.S
.A.
M.M""",
"""S.M
.A.
S.M"""]
ans2 = []

for pattern in patterns:
    ans2.append(len(grid.find_pattern_in_grid(pattern.splitlines())))
print(sum(ans2))
