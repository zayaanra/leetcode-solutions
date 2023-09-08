class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = [[1] * (i+1) for i in range(0, rowIndex+1)]
        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[rowIndex]