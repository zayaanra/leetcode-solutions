class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slower = 0
        while True:
            slow = nums[slow]
            slower = nums[slower]
            if slow == slower:
                return slower