class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2,len(dp)):
            dp[i] = min((cost[i - 1] + dp[i - 1]), (cost[i - 2] + dp[i - 2]))

        return dp[-1]






        """
        subproblem: c(k) = minimum cost to reach step k
        example for cost = [1,2,3]
       
       c(0) = 0
       c(1) = 0
       c(2) = 1 = min(cost(0) + c(0),cost(1) + c(1))
       c(3) = 2 = min(cost(1) + c(1), cost(2) + c(2))

       definition: 
        - 0 if k = 0,1
        - min(cost(k - 1) + c(k-1), cost(k-2) + c(k-2))
       
       run time:
       # of problems: n
       time for each: 1
       total: O(n)

       return value: c(-1)
       """





    

       