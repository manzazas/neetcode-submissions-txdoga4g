class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        subproblem: dp(k) = longest increasing subsequence ending at the kth letter
        examples for nums =  [9,1,4,2,3,3,7]
        dp(0) = 1
        dp(1) = 1 since 1 < 9 
        dp(2) = 2 since 4 > 1 and dp(1) + 1 = 2
        dp(3) = 2 since 2 > 1 and dp(1) + 1 = 2
        dp(4) = 3 since max(all dp's before where nums[4] > nums[u]
        dp(5) = 

        definition = 1 + max(all dps where its < current number)
        """
        

        dp = [-1] * len(nums)

        dp[0] = 1
        for i in range(1,len(nums)):
            for u in range(i - 1, -1, -1):
                if nums[u] < nums[i]:
                    dp[i] = max(dp[i], dp[u] + 1)

            if dp[i] == -1:
                dp[i] = 1

        return max(dp)

