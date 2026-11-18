class Solution:
    def findMin(self, nums: List[int]) -> int:
        #    m
        # [1,2,3,4] mid < right, is/in left part
        # [4,1,2,3]

        # [2,3,4,1] mid > right, is/in right part
        # [3,4,1,2]

        p, q = 0, len(nums) - 1

        while p < q:
            mid = (p + q) // 2

            if nums[mid] > nums[q]:
                p = mid + 1
            else:
                q = mid

        return nums[p]
