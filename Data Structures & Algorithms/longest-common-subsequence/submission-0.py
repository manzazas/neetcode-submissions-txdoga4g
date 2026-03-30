class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        """
        dp(i,j) = length of longest common subsequence
                  between the first i letters of t1 and 
                  the first j letters of t2.

        dp(1,1) = 1 because t1[1] = t2[1] 
        dp(1,2) = 1 because dp(1,1) = 1
        dp(2,1) = 1
        dp(2,2) = 1

        definition: 
            if t1[i] = t2[j]: 1 + max(dp[i-1,j],dp[i,j-1])
            otherwise: max(dp[i-1,j],dp[i,j-1])

        run time: o(n^2)

        return value: dp[-1][-1]

        """


        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(1,len(text1) + 1):
            for j in range(1,len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                   


        return dp[-1][-1]


























        