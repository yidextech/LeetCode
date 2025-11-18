class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        if n == 1:
            return True
        while True:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
            if i == n-1:
                return True
            elif i > n-1:
                return False