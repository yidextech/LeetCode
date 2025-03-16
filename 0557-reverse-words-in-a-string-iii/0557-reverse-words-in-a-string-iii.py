class Solution:
    def reverseWords(self, s: str) -> str:
        
        s= s[::-1]
        s = list(map(str, s.split()))
        s.reverse()
        s = " ".join(s)

        return s
