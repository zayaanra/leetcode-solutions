class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # time complexity - O(n)
        # space complxeity - O(1)

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if total < 0:
                total = 0
                start = i + 1
        
        return start