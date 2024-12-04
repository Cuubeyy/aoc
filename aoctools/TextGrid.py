class TextGrid:
    def __init__(self, data):
        self.matrix = data
        self.n, self.m = len(self.matrix), len(self.matrix[0])

    def find_string_in_grid(self, target):
        """
        Search for a string in a 2D grid in all 8 directions.

        Args:
            target (str): String to search for

        Returns:
            List[tuple]: List of (row, col, direction) where string starts, empty if not found
        """
        if not self.matrix or not self.matrix[0] or not target:
            return []

        rows, cols = len(self.matrix), len(self.matrix[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
            (0, -1), (0, 1),  # Left, Right
            (1, -1), (1, 0), (1, 1)  # Down-left, Down, Down-right
        ]

        def check_direction(row, col, dx, dy):
            if len(target) > max(rows, cols):
                return False

            for i in range(len(target)):
                new_row, new_col = row + i * dx, col + i * dy
                if (new_row < 0 or new_row >= rows or
                        new_col < 0 or new_col >= cols or
                        self.matrix[new_row][new_col] != target[i]):
                    return False
            return True

        results = []
        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] == target[0]:
                    for dx, dy in directions:
                        if check_direction(i, j, dx, dy):
                            results.append((i, j, (dx, dy)))

        return results

    def find_pattern_in_grid(self, pattern):
        """
        Search for a pattern in a 2D grid where '.' matches any character

        Args:
            pattern (List[str]): Pattern to search for, each string represents a row

        Returns:
            List[tuple]: List of (row, col) where pattern starts
        """
        if not self.matrix or not pattern:
            return []

        rows, cols = len(self.matrix), len(self.matrix[0])
        pattern_rows, pattern_cols = len(pattern), len(pattern[0])

        def check_pattern(start_row, start_col):
            if (start_row + pattern_rows > rows or
                    start_col + pattern_cols > cols):
                return False

            for i in range(pattern_rows):
                for j in range(pattern_cols):
                    if (pattern[i][j] != '.' and
                            self.matrix[start_row + i][start_col + j] != pattern[i][j]):
                        return False
            return True

        results = []
        for i in range(rows - pattern_rows + 1):
            for j in range(cols - pattern_cols + 1):
                if check_pattern(i, j):
                    results.append((i, j))

        return results