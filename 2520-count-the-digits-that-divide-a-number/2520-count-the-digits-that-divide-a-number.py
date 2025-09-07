class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        div = str(num)

        for d in div:
            d = int(d)
            if num%d == 0:
                count  += 1
        return count

