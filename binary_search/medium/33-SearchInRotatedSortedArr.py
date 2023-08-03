class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            if nums[mid] <= nums[r]:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    

        return -1