class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        perm = []
        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in nums:
                if n in perm:
                    continue
                perm.append(n)
                backtrack()
                perm.pop()

        backtrack()
        return res