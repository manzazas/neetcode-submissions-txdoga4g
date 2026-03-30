class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        upper = max(piles) + 1
        lower = 1
        
        res = float("inf")
        l = 1
        r = upper - 1
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        if res == float("inf"):
            return 0
        return res




