class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        triplets = []
        
        for i in range(len(nums)):
            x = nums[i]
            if i != 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                y = nums[l]
                z = nums[r]
                if x + y + z < 0:
                    l += 1
                elif x + y + z > 0:
                    r -= 1
                else:
                    triplets.append([x, y, z])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return triplets