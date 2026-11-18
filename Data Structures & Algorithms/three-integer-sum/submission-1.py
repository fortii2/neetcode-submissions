class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i in range(len(nums)):
            seen = {}

            for j in range(i + 1, len(nums)):
                target = - (nums[j] + nums[i])
        
                if target in seen:
                    res.add(tuple(sorted([nums[i], nums[j], target])))

                seen[nums[j]] = j
        
        return [[i, j, k] for i, j, k in res]