class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        best = max(piles)

        while left <= right:
            m = left + ((right - left) // 2)
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)

            if time > h:
                left = m + 1
            elif time <= h:
                best = min(best, m)
                right = m - 1
        return best

        