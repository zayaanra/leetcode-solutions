from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subboxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                if num in rows[r] or num in cols[c] or num in subboxes[(r//3, c//3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                subboxes[(r//3, c//3)].add(num)
        return True