class Solution:
    def firstUniqChar(self, s: str) -> int:
        scount = Counter(s)

        for i in range(len(s)):
            if scount[s[i]] ==1 :
                return i
        return -1