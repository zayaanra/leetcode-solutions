class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            invalid = r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or word[i] != board[r][c]
            if invalid:
                return False
            
            visited.add((r, c))
            success = backtrack(r, c+1, i+1) or\
            backtrack(r, c-1, i+1) or\
            backtrack(r+1, c, i+1) or\
            backtrack(r-1, c, i+1)
            visited.remove((r, c))

            return success

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        
        return False