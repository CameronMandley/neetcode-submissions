class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        # dp[i][a] = # of ways to form a using coins from index i onward
        dp = [[0]*(amount+1) for i in range(n+1)]
        for i in range(n+1):
            # only one way to make 0, choose no coins
            dp[i][0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount+1):
                if a >= coins[i]:
                    dp[i][a] = dp[i][a] + dp[i+1][a] + dp[i][a-coins[i]]
        return dp[0][amount]
        