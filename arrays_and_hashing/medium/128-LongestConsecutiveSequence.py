class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)
        longest = 0

        for n in s:
            x = n
            if x-1 not in s:
                seq = 1
                while x+1 in s:
                    seq += 1
                    x += 1
                longest = max(longest, seq)
        
        return longest