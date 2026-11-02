class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        currMin = float("inf")
        for i in range(len(prices)):
            currMin = min(currMin, prices[i])
            maxProf = max(maxProf, prices[i] - currMin)
        return maxProf
        