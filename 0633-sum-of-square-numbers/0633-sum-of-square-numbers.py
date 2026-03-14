class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        n = int(c ** 0.5)
        
        i = 0
        j = n

        while i <= j:
            out = i**2 + j**2
            if out == c:
                return True
            elif out < c:
                i += 1
            else:
                j -= 1
        return False