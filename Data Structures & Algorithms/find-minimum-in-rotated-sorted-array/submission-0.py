class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [ , ]

        p, q = 0, len(nums) - 1

        while p < q:
            mid = (p + q) // 2

            if nums[mid] > nums[q]:
                p = mid + 1
            else:
                q = mid

        return nums[q]
