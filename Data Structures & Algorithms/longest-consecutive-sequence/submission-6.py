class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [1,2,3,4,7] => 4
        # nums = [] => 0
        # nums = [-1, 2, 9] => 2
        # nums = [1, 1, 3, 2, 8] => 3

        sety = set(nums)
        res = 0

        for n in sety:
            if n - 1 in sety:
                continue

            count, tmp = 1, n + 1
        
            while tmp in sety:
                count += 1
                tmp += 1
            
            res = max(res, count)

        return res

            
        