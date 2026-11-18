class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p, q, res = 0, len(heights) - 1, -1

        while p < q:
            area = (q - p) * min(heights[p], heights[q])
            res = max(res, area)

            if heights[p] < heights[q]:
                p += 1
            else:
                q -= 1

        return res
