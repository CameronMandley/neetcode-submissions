class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        max_prof = 0
        for price in prices:
            curr_min = min(price, curr_min)
            curr_diff = price - curr_min
            max_prof = max(max_prof, curr_diff)
        return max_prof


        