class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        beginRow, endRow = 0, len(matrix)-1
        while beginRow <= endRow:
            midRow = beginRow + (endRow - beginRow)//2
            if matrix[midRow][0] < target:
                beginRow = midRow + 1
            elif matrix[midRow][0] > target:
                endRow = midRow - 1
            else:
                break


        midRow = beginRow + (endRow - beginRow)//2
        l, r = 0, len(matrix[midRow])-1
        while l <= r:
            m = l + (r - l)//2
            if matrix[midRow][m] > target:
                r = m - 1
            elif matrix[midRow][m] < target:
                l = m + 1
            else:
                return True
        
        return False