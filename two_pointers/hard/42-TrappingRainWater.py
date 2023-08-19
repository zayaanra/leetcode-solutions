class Solution:
    def trap(self, height: list[int]) -> int:
        trapped = 0
        l, r = 0, len(height)-1
        LMAX, RMAX = height[l], height[r]

        while l < r:
            if LMAX < RMAX:
                l += 1
                LMAX = max(LMAX, height[l])
                trapped += (LMAX - height[l])
            else:
                r -= 1
                RMAX = max(RMAX, height[r])
                trapped += (RMAX - height[r])
            
        return trapped