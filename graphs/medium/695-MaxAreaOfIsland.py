class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == 1:
                    area = max(area, dfs(row, col))

        return area