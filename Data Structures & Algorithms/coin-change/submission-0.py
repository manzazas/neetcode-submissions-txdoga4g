class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for value in coins:
                if i - value >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - value])
                else:
                    continue

        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]
             

        

        