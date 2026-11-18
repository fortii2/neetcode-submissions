from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            fre = [0] * 26

            for c in s:
                fre[ord(c) - ord("a")] += 1
            m[tuple(fre)].append(s)

        return list(m.values())
