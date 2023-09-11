class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coords = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    coords.add((r, c))

        for r, c in coords:
            matrix[r] = [0] * len(matrix[r])
            for nr in range(len(matrix)):
                matrix[nr][c] = 0