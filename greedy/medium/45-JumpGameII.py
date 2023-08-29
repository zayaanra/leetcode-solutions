class Solution:
    def jump(self, nums: list[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, nums[i] + i)
            l = r + 1
            r = maxJump
            res += 1
        return res