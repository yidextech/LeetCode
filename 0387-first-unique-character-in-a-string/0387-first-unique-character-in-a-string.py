class Solution:
    def firstUniqChar(self, s: str) -> int:

        
        hashTable = {}

        for n in s:
            if n in hashTable:
                hashTable[n] += 1
            else:
                hashTable[n] = 1
        for m,k in hashTable.items():
            if k == 1:
                return s.index(m)
        return -1