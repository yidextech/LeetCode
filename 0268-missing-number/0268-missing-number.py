class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums) #n
        nums = set(nums) #n
        for i in range(num+1):
            if i not in nums:
                return i
        