class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # time complexity - O(nlogn)
        # space complexity - O(n)

        pairs = [(p, s) for p, s in zip(position, speed)]
        fleets = 0
        curTime = 0
        
        for pos, spd in sorted(pairs, reverse=True):
            eta = (target-pos)/spd
            if eta > curTime:
                curTime = eta
                fleets += 1

        return fleets