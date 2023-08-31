import math
import heapq

class Solution:
    def getDistance(self, x1, y1):
        distX = pow(x1 - 0, 2)
        distY = pow(y1 - 0, 2)
        return math.sqrt(distX + distY)
        

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # time complexity - O(nlogn)
        # space complexity - O(n + k)

        heap = []
        closest = []

        for x, y in points:
            dist = self.getDistance(x, y)
            heap.append([dist, x, y])
        
        heapq.heapify(heap)

        while k > 0:
            dist, x, y = heapq.heappop(heap)
            closest.append([x, y])
            k -= 1
        
        return closest