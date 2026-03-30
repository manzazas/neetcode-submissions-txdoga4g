class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def memoization(step):
            if step <= 2:
                return step
            if step not in cache:
                cache[step] = memoization(step - 1) + memoization(step - 2)
            return cache[step]

        return memoization(n)
        