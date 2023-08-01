class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        topK = []

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
 
        for n in count:
            value = count[n]
            freq[value].append(n)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK