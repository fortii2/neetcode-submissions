from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapy = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            mapy[key].append(s)
        
        return list(mapy.values())