class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last = s.split(" ")
        return len(last[-1])
