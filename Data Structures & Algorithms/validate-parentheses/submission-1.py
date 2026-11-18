class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {"]": "[", ")": "(", "}": "{"}

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack or stack.pop() != pairs[char]:
                    return False
            
        return not stack

