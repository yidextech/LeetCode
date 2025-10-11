class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [None]*n

        for i in range(n):
            nums[i] = start + 2 *i
        
        res = 0
        for num in nums:
            res ^= num
        return res