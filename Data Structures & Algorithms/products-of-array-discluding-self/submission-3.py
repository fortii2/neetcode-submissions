class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        pre = 1
        for i, n in enumerate(nums):
            res[i] = pre
            pre *= n

        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]

        return res
