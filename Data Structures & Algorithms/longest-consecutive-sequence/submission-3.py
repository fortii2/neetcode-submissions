class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put in set
        sety = set(nums)
        res = 0

        # fidn start
        for n in nums:
            if n - 1 in sety:
                continue

            nxt = n + 1
            tmp_res = 1

            while nxt in sety:
                nxt += 1
                tmp_res += 1

            res = max(res, tmp_res)
        return res
