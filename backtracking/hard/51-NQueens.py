class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["."] * n for i in range(n)]
        res = []

        colSet = set()
        posDiagSet = set()
        negDiagSet = set()

        def backtrack(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in colSet or (r+c) in posDiagSet or (r-c) in negDiagSet:
                    continue

                colSet.add(c)
                posDiagSet.add(r+c)
                negDiagSet.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)

                colSet.remove(c)
                posDiagSet.remove(r+c)
                negDiagSet.remove(r-c)
                board[r][c] = "."


        backtrack(0)

        return res