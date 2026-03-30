class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        """

        p(k) = largest product ending at index k

        n(k) = smallest product ending at index k

        nums = [1,2,-3,4,-5] (120)
        p(1) = 1
        n(1) = 1
        p(2) = 2
        n(2) = 1
        p(3) = -3 max(-3 * 2, -3, -3 * 1 )
        n(3) = -6 min(-3 * 2, 1)
        p(4) = 4 max(4, 4 * -3, 4 * -6)
        n(4) = -24 min(4,4 * -3, 4 * -6)
        p(5) = 120 max (-5, -5 * -24, -5 * 4)
        n(5) = -20 min(-5, -5 * -24, -5 * 24)


        o(2n) = o(n)

        return value: max(p)

        """

        p = [-1] * len(nums)
        n = [-1] * len(nums)


        p[0] = nums[0]
        n[0] = nums[0]

        for i in range(1,len(nums)):
            p[i] = max(nums[i],nums[i] * p[i-1], nums[i] * n[i-1])
            n[i] = min(nums[i], nums[i] * p[i-1], nums[i] * n[i-1])


        return max(p)















        