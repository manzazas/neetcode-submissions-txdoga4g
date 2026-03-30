class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        while min_k < max_k:
            cur_k = (max_k + min_k) // 2
            cur_hour = 0
            for p in piles:
                cur_hour += (p + cur_k - 1) // cur_k

            if cur_hour > h:
                min_k = cur_k + 1
            else:
                max_k = cur_k

        return min_k




