class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        if len(words) == 1:
            return words
        
        i = 1
        j = 0
        count = 0
        while i<len(words) and j<len(words):
            j = i-1
            if sorted(words[i]) == sorted(words[j]):
                del words[i]
                count += 1
                if count == len(words): return words
            else:
                i+=1 
        return words
