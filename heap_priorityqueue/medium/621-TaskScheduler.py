from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        c = Counter(tasks)
        maxHeap = [-cnt for cnt in c.values()]
        heapq.heapify(maxHeap)
        q = deque()

        units = 0
        while maxHeap or q:
            units += 1
            if not maxHeap:
                units = q[0][1]
            else:
                taskCount = 1 + heapq.heappop(maxHeap)
                if taskCount != 0:
                    q.append((taskCount, units + n))
            if q and q[0][1] == units:
                heapq.heappush(maxHeap, q.popleft()[0])
        return units