class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                topIdx, topHeight = stack.pop()
                area = max(area, (i - topIdx) * topHeight)
                start = topIdx
            stack.append((start, height))
        
        for i, height in stack:
            area = max(area, height * (len(heights) - i))
        return area