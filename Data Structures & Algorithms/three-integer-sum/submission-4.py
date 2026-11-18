class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            p, q = i + 1, len(nums) - 1

            while p < q:
                sumy = nums[p] + nums[q] + nums[i]

                if sumy == 0:
                    res.append([nums[p], nums[q], nums[i]])
                    p += 1
                    q -= 1

                    while p < q and nums[p] == nums[p - 1]:
                        p += 1

                    while p < q and nums[q] == nums[q + 1]:
                        q -= 1

                elif sumy < 0:
                    p += 1
                else:
                    q -= 1

        return res
