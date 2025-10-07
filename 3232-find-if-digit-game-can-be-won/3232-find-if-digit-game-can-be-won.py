class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = sum(x for x in nums if len(str(x)) == 1)
        double = sum(x for x in nums if len(str(x)) == 2)
        rem1 = sum(nums) - single
        rem2 = rem1+single-double

        if rem1 < single or rem2 < double:
            return True
        return False