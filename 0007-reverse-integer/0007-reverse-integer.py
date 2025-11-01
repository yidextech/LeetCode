class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        res = x[::-1]
        val = 0

        if res[-1] == '-':
            res =res.replace('-','')
            val = -1*int(res)
        else:
            val = int(res)
        if val > (2**31) -1 or val < -(2**31):
            return 0
        return val