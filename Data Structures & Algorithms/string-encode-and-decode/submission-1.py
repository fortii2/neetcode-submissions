class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    # 1#a 2#ab
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = 0

            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1

            i += 1
            res.append(s[i : i + length])
            i += length

        return res
