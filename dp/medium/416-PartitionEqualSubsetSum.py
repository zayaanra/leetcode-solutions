class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2
        dp = set()
        dp.add(0)

        total = 0

        for i in range(len(nums)-1, -1, -1):
            newDP = set()
            for n in dp:
                if n + nums[i] == target:
                    return True
                newDP.add(n + nums[i])
                newDP.add(n)
            dp = newDP
        return False