class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cheapest = prices[0]

        for price in prices[1:]:
            today = price - cheapest
            res = max(res, today)

            cheapest = min(cheapest, price)

        return res