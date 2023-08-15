class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0

        for amount in range(1, len(memo)):
            for coin in coins:
                # we can only consider the current coin if its value is less than the current amount
                if coin <= amount:
                    # basically, we are calculating the change (amount - coin)
                    # the value stored at memo[change] indicates the minimum amount of coins needed to make that change
                    # since we are calculating this for the current amount, we do 1 extra coin + memo[change]
                    # then, we take the min of the current memo[amount] and 1 + memo[change]
                    # this gives the minimum number of coins needed to make the current amount
                    memo[amount] = min(1 + memo[amount - coin], memo[amount])
        
        if memo[amount] == amount + 1:
            return -1
        return memo[amount]