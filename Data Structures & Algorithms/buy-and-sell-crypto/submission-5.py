class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r <= len(prices)-1:
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0:
                l = r
                r += 1
            else:
                profit = max(profit, curr_profit)
                r += 1
        return profit

        