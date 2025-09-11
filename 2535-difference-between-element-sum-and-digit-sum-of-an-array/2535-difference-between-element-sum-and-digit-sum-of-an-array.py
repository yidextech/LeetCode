class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = sum(nums)
        dig_sum = 0
        for num in nums:
            num = str(num)
            for i in num:
                dig_sum += int(i)
        return abs(ele_sum-dig_sum)