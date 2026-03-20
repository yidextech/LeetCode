class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        j = 0
        turn  = 1
        res =""

        while i<len(word1) or j<len(word2):
            turn = 0 if turn == 1 else 1
            if i<len(word1) and turn == 0:
                res += word1[i]
                i += 1
            elif j <len(word2):
                res += word2[j]
                j += 1
        return res