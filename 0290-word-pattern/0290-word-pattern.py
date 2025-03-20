class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = list(map(str, s.split()))

        hashTable = {
            s[0] : pattern[0]
        }
        takenLetters = {pattern[0]}
        if len(s) == len(pattern):

            for i in range(1, len(s)):
                if s[i] in hashTable:
                    if hashTable[s[i]] != pattern[i]:
                        return False
                else:
                    if pattern[i] not in takenLetters:
                        hashTable[s[i]] = pattern[i]
                        takenLetters.add(pattern[i])
                    else:
                        return False
            return True
        else:
            return False