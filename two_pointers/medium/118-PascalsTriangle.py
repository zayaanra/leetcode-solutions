class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # time complexity -  O(n^2)
        # space complexity - O(n^2)
        rows = [[1] * n for n in range(1, numRows+1)]
        for r in range(2, numRows):
            for c in range(1, len(rows[r])-1):
                rows[r][c] = rows[r-1][c-1] + rows[r-1][c] 
        return rows