class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0 or len(prices) == 1:
            return 0

        buy = 0
        
        max_profit = 0
        for i in range(0,len(prices) - 1):
            for j in range(i + 1, len(prices)):
                curr_profit = prices[j] - prices[i]
                if curr_profit > max_profit:
                    max_profit = curr_profit

                    


        return max_profit


        



        
        