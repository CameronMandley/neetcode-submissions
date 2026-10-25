class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(lowest, price)
            max_prof = max(max_prof, price - lowest)
        return max_prof
        