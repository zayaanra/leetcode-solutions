class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or ((r, c)) in visited or grid[r][c] == "0":
                return
            
            visited.add((r, c))

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

            
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands