class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                    nums[i] *=2
                    nums[i+1] = 0
        new_nums = [num for num in nums if num != 0]

        for i in range(len(nums)-len(new_nums)):
            new_nums.append(0)
        return new_nums