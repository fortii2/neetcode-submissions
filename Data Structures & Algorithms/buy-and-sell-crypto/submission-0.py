class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for cur in prices:
            profit = cur - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, cur)

        return max_profit