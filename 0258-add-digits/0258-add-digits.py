class Solution:
    def addDigits(self, num: int) -> int:
        
        num_s = str(num)

        while len(num_s)>1:
            num = sum(list(map(int, num_s)))
            num_s = str(num)

        return num