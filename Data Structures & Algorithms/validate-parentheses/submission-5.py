class Solution:
    def isValid(self, s: str) -> bool:
        mapy = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch not in mapy:
                stack.append(ch)
                continue
            
            if not stack:
                return False
            
            if stack.pop() != mapy[ch]:
                return False
            
        return not stack