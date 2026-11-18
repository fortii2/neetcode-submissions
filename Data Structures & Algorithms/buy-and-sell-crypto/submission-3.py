class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cheapest = float('inf')

        for price in prices:
            today = price - cheapest
            res = max(res, today)

            cheapest = min(cheapest, price)

        return res