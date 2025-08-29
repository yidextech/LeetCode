class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if stack and brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
            
