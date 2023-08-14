class Solution:
    def rob(self, nums: list[int]) -> int:
        m1, m2 = 0, 0
        for n in nums:
            tmp = max(n + m1, m2)
            m1 = m2
            m2 = tmp
        return m2