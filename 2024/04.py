def search(grid):
    def check_direction(row, col, dx, dy):
        if 0 <= row + 3 * dx < rows and 0 <= col + 3 * dy < cols:
            for i in range(4):
                if grid[row + i * dx][col + i * dy] != word[i]:
                    return False
            return True
        return False

    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    results = []
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    results.append((i, j))

    return results


def search_x(grid):
    rows = len(grid)
    cols = len(grid[0])
    results = []

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] != 'A':
                continue

            tl_br = [grid[i - 1][j - 1], grid[i][j], grid[i + 1][j + 1]]
            tr_bl = [grid[i - 1][j + 1], grid[i][j], grid[i + 1][j - 1]]

            tl_br_valid = ''.join(tl_br) in ['MAS', 'SAM']
            tr_bl_valid = ''.join(tr_bl) in ['MAS', 'SAM']

            if tl_br_valid and tr_bl_valid:
                results.append((i, j))

    return results


grid = open("04.in").read().splitlines()
print(len(search(grid)))
print(len(search_x(grid)))
