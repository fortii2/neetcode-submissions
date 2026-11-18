class Solution:
    def isValid(self, s: str) -> bool:
        # "[]()" -> true
        # "[({})]" -> true

        # "}" -> false
        # "[" -> false
        # ")(" -> false

        # "[](" -> false
        # ")()" -> false

        if len(s) % 2 != 0:
            return False

        pairs = {")": "(", "}": "{", "]": "["}

        stack = []

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False

        return not stack
