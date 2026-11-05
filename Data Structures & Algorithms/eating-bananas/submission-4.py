class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)

        left, right = 1, upper_bound

        def eat_bananas(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            return total

        while left < right:
            mid = (left + right) // 2
            num_hours = eat_bananas(mid)
            if num_hours <= h:
                right = mid
            else:
                left = mid + 1
        return left