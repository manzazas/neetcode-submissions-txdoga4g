class Solution:
    def countSubstrings(self, s: str) -> int:
        """

        dp(i,j) = Is between the ith and jth index a palindrome

        s = "abc"
        dp(0,0) = True
        dp(1,1) = True
        dp(2,2) = True
        dp(0,1) = s(0) = s(1) = False
        dp(1,2) = s(1) = s(2) = False
        dp(0,2) = dp(1,1) and s(i) == s(j) = False

        


        defintion: True if i == j.
                   s(i) == s(j) if j is 1 more than s, j = i + 1
                   dp(i+1,j-1) and s(i) == s(j) else

        runtime: subproblems: n^2
                 time for each: o(1)
                 total: O(n^2)

        return: 
        """



        dp = [[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s) - 1,-1,-1):
            for j in range(i,len(s)):
                if i == j:
                    dp[i][j] = True
                elif  j == i + 1:
                    dp[i][j] = (s[i] == s[j])
                if dp[i][j] == False and j > i:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]


        count = 0
        for i in range(0,len(dp)):
            for j in range(0,len(dp[0])):
                if dp[i][j] == True:
                    count += 1



        return count
        
                


        
                




















        