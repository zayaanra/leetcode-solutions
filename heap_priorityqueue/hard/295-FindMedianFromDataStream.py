import heapq

class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            # pop max from maxHeap and add to minHeap
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val * -1)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            # pop min from minHeap and add to maxHeap
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        return ((-1 * self.maxHeap[0]) + self.minHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()