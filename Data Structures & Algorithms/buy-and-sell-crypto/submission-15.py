class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right += 1

            elif prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit,max_profit)
                right += 1
        return max_profit
            



