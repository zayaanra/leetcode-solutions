import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # time complexity - O(nlogn)
        # space complexity - O(n)
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while stones:
            print(stones)
            if len(stones) == 1:
                return abs(stones[0])
            else:
                x, y = heapq.heappop(stones), heapq.heappop(stones)
                if x != y:
                    heapq.heappush(stones, abs(y-x) * -1)
        return 0