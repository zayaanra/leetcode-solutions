class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        low = prices[0]
        # we make the most profit if we buy the lowest price and sell at the highest price
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            profit = max(profit, prices[i] - low)
        
        return profit