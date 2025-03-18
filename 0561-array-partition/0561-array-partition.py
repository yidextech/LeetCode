class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        sum = 0
        i = 0
        while True:
            if i < len(nums):
                sum += nums[i]
                i += 2
            else:
                return sum