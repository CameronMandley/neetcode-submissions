class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        output = right

        while left <= right:
            mid = (left + right)//2
            time = 0
            for pile in piles:
                time += math.ceil(float(pile)/mid)
            if time <= h:
                output = mid
                right = mid - 1
            else:
                left = mid + 1
        return output