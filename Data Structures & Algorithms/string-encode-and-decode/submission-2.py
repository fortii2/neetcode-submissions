class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res = res + str(len(s)) + "#" + s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        l = 0

        while i < len(s):
            if s[i] != "#":
                l = l * 10 + int(s[i])
                i += 1
            else:
                i += 1
                res.append(s[i : i + l])
                i += l
                l = 0
        return res
