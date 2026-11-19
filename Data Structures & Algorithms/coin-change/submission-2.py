class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(amount+1):
            if i in coins:
                continue
            minCoins = float("inf")
            # consider all possibilities of last coin added
            for coin in coins:
                if coin > i:
                    continue
                # find the remaining amount that must be added to make i
                diff = i - coin
                # find the min number of coins to make that diff
                numCoins = dp[diff]
                minCoins = min(numCoins+1, minCoins)
            # dp[i] = min number of coins to make i
            dp[i] = minCoins
        return dp[amount] if dp[amount] != float("inf") else -1
        