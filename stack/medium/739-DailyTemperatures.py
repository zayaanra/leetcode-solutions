class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # time complexity - O(n)
        # space complexity - O(n)
        
        answer = [0] * len(temperatures)
        stack = []
        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                prevTmp, prevTmpIdx = stack.pop()
                answer[prevTmpIdx] = i - prevTmpIdx
            stack.append((tmp, i))
        return answer