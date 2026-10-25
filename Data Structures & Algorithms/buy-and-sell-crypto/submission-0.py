class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            output = max(output, price - lowest)
        return output
        
        