
def hill_climb(input):
    start = [0, 0]
    goal = [len(input[0]) - 1, len(input) - 1]
    row_len = len(input[0])
    col_len = len(input)
    visited = [[False for i in range(col_len)] for j in range(row_len)]
    visited[start[0]][start[1]] = True
    path = [start]
    steps = 0
    while path[-1] != goal:
        steps += 1
        # Get all valid adjacent squares
        adj = []
        for x, y in [(0,-1), (0,1), (-1,0), (1,0)]:
            x2 = path[-1][0] + x
            y2 = path[-1][1] + y
            if 0 <= x2 < row_len and 0 <= y2 < col_len:
                # Make sure the elevation is at most one higher
                if ord(input[y2][x2]) - ord(input[path[-1][1]][path[-1][0]]) <= 1:
                    # Make sure we haven't already visited it
                    if not visited[x2][y2]:
                        visited[x2][y2] = True
                        adj.append((x2, y2))
        # Try the next step
        if adj:
            path.append(adj[0])
        else:
            # No valid adjacent squares, so backtrack
            path.pop()
    return steps

input = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

print(hill_climb(input)) # 31