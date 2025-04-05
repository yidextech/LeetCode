class Solution:
    def longestPalindrome(self, s: str) -> str:
        longPal = ""
        for i in range(len(s)):
            if len(longPal) >= len(s[i:]):
                return longPal
            for j in range(i, len(s)):
                subS = s[i:j+1] 
                if subS == subS[::-1]:
                    if len(subS) > len(longPal):
                        longPal = subS
        return longPal