class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #    m
        # [1,2,3,4] mid < right, [mid, right] ordered
        # [3,4,1,2]

        # [2,3,4,1] mid > right, [left, mid] ordered
        # [4,1,2,3]

        p, q = 0, len(nums) - 1

        while p <= q:
            mid = (p + q) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[q]:
                # left side ordered
                if nums[p] <= target < nums[mid]:
                    q = mid - 1
                else:
                    p = mid + 1
            else:
                # right side ordered
                if nums[mid] < target <= nums[q]:
                    p = mid + 1
                else:
                    q = mid - 1
        
        return -1