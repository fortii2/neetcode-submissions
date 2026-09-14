class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue

            cur = num
            length = 1
            while cur + 1 in nums_set:
                length += 1
                cur += 1

            longest = max(longest, length)

        return longest
