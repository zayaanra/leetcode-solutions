class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

            # exclude duplicates
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return res