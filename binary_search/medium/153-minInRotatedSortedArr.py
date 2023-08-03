class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        h = len(nums)-1
        m = 0

        while l < h:
            if nums[l] < nums[h]:
                return nums[l]

            m = l + (h - l) // 2
            cur = nums[m]
            head = nums[l]
            tail = nums[h]
            if cur > tail:
                l = m+1
            elif cur < tail:
                h = m
        
        return nums[l]