class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        output = 0
        for price in prices:
            lowest = min(lowest, price)
            output = max(output, price-lowest)
        return output
        