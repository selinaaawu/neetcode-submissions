class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        ## BINARY SEARCH | time: O(logn), space: O(1)
        # search answer array [1, max(piles)], find minimum eating rate k
        # for rate k, calculate total hours to consume all piles
        # if less than h, try to eat less
        # otherwise, taking too long, eat more
        l, r = 1, max(piles)

        while l < r:
            # banana per hour eating rate
            k = l + (r - l) // 2
            
            hours = 0
            for pile in piles:
                # math.ceil(pile / k) operation
                hours += (pile + k - 1) // k

            if hours <= h:
                r = k
            else:
                l = k + 1

        return l
        