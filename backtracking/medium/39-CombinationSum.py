class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res = []
        cdts = []
        total = 0

        def backtrack(i):
            nonlocal total
            if total == target:
                res.append(cdts.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            total += candidates[i]
            cdts.append(candidates[i])
            backtrack(i)

            total -= cdts[-1]
            cdts.pop()
            backtrack(i+1)

        backtrack(0)
        return res