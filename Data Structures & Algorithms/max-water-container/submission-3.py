class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        p, q = 0, len(heights) - 1
        
        while p < q:
            fields = min(heights[p], heights[q]) * (q - p)
            res = max(res, fields)
            
            if heights[p] < heights[q]:
                p += 1
            else:
                q -= 1
        
        return res
        