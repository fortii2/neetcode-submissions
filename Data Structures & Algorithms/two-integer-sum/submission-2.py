class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            minus = target - n
            
            if minus in seen:
                return [seen[minus], i]
            
            seen[n] = i
        
        return []