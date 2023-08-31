import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # time complexity - O(nlogn)
        # space complexity - O(n)
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]