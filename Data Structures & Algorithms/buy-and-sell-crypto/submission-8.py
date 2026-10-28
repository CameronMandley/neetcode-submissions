class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = float("inf")
        max_prof = 0
        for price in prices:
            prev_min = min(price, prev_min)
            max_prof = max(max_prof, (price - prev_min))
        return max_prof

        