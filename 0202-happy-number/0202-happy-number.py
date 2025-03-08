class Solution:
    def isHappy(self, n: int) -> bool:
        
        n = str(n)
        count = 0
        while True:
            newN = 0
            for i in range(len(n)):
                newN += int(n[i])**2
            n = str(newN)
            if n == "1":
                return True
            else:
                count += 1
                if count == 10:
                    return False
            
