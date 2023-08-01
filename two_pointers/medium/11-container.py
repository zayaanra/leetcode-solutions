class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height)-1

        area = 0
        while l < r:
            x, y = height[l], height[r]
            dist = r - l
            if x > y:
                diff = x - y
                area = max(area, (x-diff) * dist)
                r -= 1
            elif y >= x:
                diff = y - x
                area = max(area, (y-diff) * dist)
                l += 1
        return area