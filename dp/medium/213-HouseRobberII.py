class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        def robHelper(nums):
            m1, m2 = 0, 0
            for n in nums:
                tmp = max(n + m1, m2)
                m1 = m2
                m2 = tmp
            return m2
        
        return max(robHelper(nums[0:len(nums)-1]), robHelper(nums[1:len(nums)]))