class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for i in range(n-2, -1, -1):
            tmp = x + y
            y = x
            x = tmp
        return x