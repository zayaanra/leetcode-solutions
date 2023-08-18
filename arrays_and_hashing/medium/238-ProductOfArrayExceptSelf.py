class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = []
        left = [1 for n in nums]
        right = [1 for n in nums]

        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        for i in range(len(nums)):
            products.append(left[i] * right[i])

        return products