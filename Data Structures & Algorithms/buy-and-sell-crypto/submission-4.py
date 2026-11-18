class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float("inf")

        for p in prices:
            profit = p - minPrice
            res = max(res, profit)
            minPrice = min(minPrice, p)

        return res
