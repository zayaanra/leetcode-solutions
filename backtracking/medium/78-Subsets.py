class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            backtrack(i+1)

            # exclude nums[i]
            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return res