class Solution:
    def isValid(self, s: str) -> bool:

        smap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []

        for i in range(len(s)):
            if s[i] not in smap:
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    if stack[-1] == smap[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:

                    return False
                
        return len(stack) == 0