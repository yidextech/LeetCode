class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        gPairs = 0

        for i in range(len(nums)-1):
            gPairs += nums[i+1:].count(nums[i])
        return gPairs