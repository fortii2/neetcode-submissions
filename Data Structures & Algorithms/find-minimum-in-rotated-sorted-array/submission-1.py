class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mid needs to compare with left/right, so [,]
        p, q = 0, len(nums) - 1

        while p < q:
            mid = (p + q) // 2

            if nums[mid] < nums[q]:
                q = mid
            else:
                p = mid + 1
        
        return nums[q]