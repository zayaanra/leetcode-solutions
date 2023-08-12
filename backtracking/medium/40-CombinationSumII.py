class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        total = 0
        combo = []
        res = []

        candidates.sort()

        def backtrack(i):
            nonlocal total
            if total == target:
                res.append(combo.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            combo.append(candidates[i])
            total += candidates[i]
            backtrack(i+1)
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            total -= combo[-1]
            combo.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res