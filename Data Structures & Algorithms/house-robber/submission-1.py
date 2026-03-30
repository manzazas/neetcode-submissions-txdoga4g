class Solution:
    def rob(self, nums: List[int]) -> int:

        dp_plus = [-1] * len(nums)
        dp_minus = [-1] * len(nums)
        dp_plus[0] = nums[0]
        dp_minus[0] = 0
        for i in range(1,len(nums)):
            dp_plus[i] = nums[i] + dp_minus[i - 1]
            dp_minus[i] = max(dp_plus[i - 1],dp_minus[i - 1])

        return max(dp_plus[-1],dp_minus[-1])
        
