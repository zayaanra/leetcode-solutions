import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r-l)//2
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            if time <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res