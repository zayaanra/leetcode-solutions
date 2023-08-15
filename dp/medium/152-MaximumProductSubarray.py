class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        LMAX, RMAX, MAX = 1, 1, max(nums[l], nums[r])
        while l < len(nums) and r >= 0:
            LMAX = 1 if LMAX == 0 else LMAX
            RMAX = 1 if RMAX == 0 else RMAX
            LMAX *= nums[l]
            RMAX *= nums[r]

            MAX = max(MAX, LMAX, RMAX)
            l += 1
            r -= 1
        
        return MAX