class Solution:
    def tribonacci(self, n: int) -> int:
        x, y, z = 0, 1, 1
        for i in range(n-2):
            tmp = x + y + z
            x = y
            y = z
            z = tmp
        return z if n != 0 else 0