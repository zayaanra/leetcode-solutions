class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # time complexity - O(n)
        # space complexity - 

        t = set()
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i, num in enumerate(triplet):
                if num == target[i]:
                    t.add(i)
        
        return len(t) == 3