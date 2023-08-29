class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curSum = 0
        maxSum = float("-inf")
        for n in nums:
            curSum = max(n, curSum + n)
            maxSum = max(maxSum, curSum)
        return maxSum